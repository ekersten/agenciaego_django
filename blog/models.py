import random

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
    short_description = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=random.randint(900, 1500))

    content = StreamField(
        [
            ('text', CharBlock(required=False, max_length=100))
        ],
        blank=True,
        null=True
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('is_use_case'),
        FieldPanel('likes'),
        StreamFieldPanel('content')
    ]

    @property
    def formatted_title(self):
        return '<h1 class="header__title">{}</h1>'.format(self.title)

    class Meta:
        verbose_name = 'Blog Page'
        verbose_name_plural = 'Blog Pages'
