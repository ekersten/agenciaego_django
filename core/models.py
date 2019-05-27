from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

class BasePage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover')
    ]


class ServicesPage(Page):
    template = 'core/services.html'
    max_count = 1
    subpage_types = []

    class Meta:
        verbose_name = 'Services Page'
        verbose_name_plural = 'Services Pages'


class AboutPage(Page):
    template = 'core/about.html'
    max_count = 1
    subpage_types = []

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'


class ProjectDiscoveryPage(Page):
    template = 'core/project_discovery.html'
    max_count = 1
    subpage_types = []

    class Meta:
        verbose_name = 'Project Discovery Page'
        verbose_name_plural = 'Project Discovery Pages'
