from django.db import models
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from core.models import BasePage
# Create your models here.


from streams.blocks import (
    TitleBlock,
    SubtitleBlock,
    SimpleRichTextBlock,
    BlockQuoteBlock,
    YoutubeEmbedBlock,
    FullWidthImageBlock,
    TextImageBlock,
    TitleImageBlock,
    ProjectBlock,
)

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

    short_description = models.TextField(blank=True, null=True)

    content = StreamField(
        [
            ('title', TitleBlock()),
            ('subtitle', SubtitleBlock()),
            ('text', SimpleRichTextBlock()),
            ('quote', BlockQuoteBlock()),
            ('video', YoutubeEmbedBlock()),
            ('fw_image', FullWidthImageBlock()),
            ('text_image', TextImageBlock()),
            ('title_image', TitleImageBlock()),
            ('project', ProjectBlock()),
        ],
        blank=True,
        null=True
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('short_description'),
        StreamFieldPanel('content')
    ]

    @property
    def formatted_title(self):
        return '<h1 class="header__title">{}</h1>'.format(self.title)

    def save(self, *args, **kwargs):
        metadata_key = make_template_fragment_key('job_page_metadata', [self.id])
        content_key = make_template_fragment_key('job_page_content', [self.id])
        cache.delete(metadata_key)
        cache.delete(content_key)

        return super().save(*args, **kwargs)

        
    class Meta:
        verbose_name = 'Job Page'
        verbose_name_plural = 'Job Pages'
