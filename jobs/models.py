from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from core.models import BasePage
# Create your models here.


class JobsListingPage(Page):
    template = 'jobs/jobs_listing_page.html'

    subpage_types = ['jobs.JobPage']

    max_count = 1

    class Meta:
        verbose_name = 'Jobs Listing Page'
        verbose_name_plural = 'Jobs Listing Pages'


class JobPage(BasePage):
    template = 'jobs/job_page.html'

    subpage_types = []
    parent_page_types = ['jobs.JobsListingPage']

    content = StreamField(
        [
            ('text', CharBlock(required=False, max_length=100))
        ],
        blank=True,
        null=True
    )

    content_panels = BasePage.content_panels + [
        StreamFieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Job Page'
        verbose_name_plural = 'Job Pages'
