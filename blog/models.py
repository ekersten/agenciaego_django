from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from core.models import BasePage
# Create your models here.


class BlogListingPage(Page):
    template = 'blog/blog_listing_page.html'

    subpage_types = ['blog.BlogPage']
    
    max_count = 1
    class Meta:
        verbose_name = 'Blog Listing Page'
        verbose_name_plural = 'Blog Listing Pages'


class BlogPage(BasePage):
    template = 'blog/blog_page.html'

    subpage_types = []
    parent_page_types = ['blog.BlogListingPage']

    is_use_case = models.BooleanField(default=False)

    content = StreamField(
        [
            ('text', CharBlock(required=False, max_length=100))
        ],
        blank=True,
        null=True
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('is_use_case'),
        StreamFieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Blog Page'
        verbose_name_plural = 'Blog Pages'
