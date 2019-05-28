from django.db import models
from django_extensions.db.fields import AutoSlugField
from wagtailorderable.models import Orderable
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.translation import ugettext as _
from wagtailmodelchooser import register_model_chooser
from wagtailmodelchooser.edit_handlers import ModelChooserPanel
# Create your models here.

from core.models import BasePage
@register_model_chooser
class BehanceProject(Orderable, models.Model):
    behance_id = models.PositiveIntegerField(editable=False)
    behance_name = models.CharField(max_length=255, editable=False)
    behance_url = models.URLField(blank=True, null=True, editable=False)
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', overwrite=True)
    client = models.ForeignKey(
        'behance.Client',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('description'),
                ModelChooserPanel('client')
            ],
            heading=_('Project Data')
        ),
        ImageChooserPanel('cover')
    ]

    class Meta:
        verbose_name = 'Behance Project'
        verbose_name_plural = 'Behance Projects'

    def __str__(self):
        return self.name
    
class BehanceProjectModule(Orderable, models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    project = models.ForeignKey(BehanceProject, related_name='modules', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Behance Project Module'
        verbose_name_plural = 'Behance Project Modules'


@register_model_chooser
class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo')
    ]

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class BehanceProjectListingPage(Page):

    template = 'behance/project_listing_page.html'
    max_count = 1
    subpage_types = ['behance.BehanceProjectPage']
    class Meta:
        verbose_name = 'Behance Projects Listing Page'
        verbose_name_plural = 'Behance Projects Listing Pages'


class BehanceProjectPage(BasePage):

    template = 'behance/project_page.html' 
    parent_page_types = ['behance.BehanceProjectListingPage']


    project = models.ForeignKey(
        BehanceProject,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured_in_services = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('featured_in_services'),
        ModelChooserPanel('project')
    ]
    class Meta:
        verbose_name = 'Behance Project Page'
        verbose_name_plural = 'Behance Project Pages'
