from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from employees.models import Employee
# prevent circular import
from behance import models as behance_models

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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['projects'] = behance_models.BehanceProjectPage.objects.live(
        ).public().filter(featured_in_services=True).all()
        return context
    class Meta:
        verbose_name = 'Services Page'
        verbose_name_plural = 'Services Pages'


class AboutPage(Page):
    template = 'core/about.html'
    max_count = 1
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['partners'] = Employee.objects.filter(type=1)
        context['leads'] = Employee.objects.filter(type=2)
        context['teams'] = Employee.objects.filter(type=3)

        return context
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
