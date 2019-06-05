import random

from django.db import models
from django import forms
from django.utils.translation import ugettext as _
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    MultiFieldPanel,
    InlinePanel
) 

from modelcluster.models import ParentalManyToManyField, ParentalKey

from core.models import BasePage


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


class BlogListingPage(Page):
    template = 'blog/blog_listing_page.html'

    subpage_types = ['blog.BlogPage']
    
    max_count = 1
    class Meta:
        verbose_name = 'Blog Listing Page'
        verbose_name_plural = 'Blog Listing Pages'

class BlogPageLink(Orderable):
    page = ParentalKey('blog.BlogPage', related_name='links')
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    target = models.CharField(
        max_length=6,
        choices=[
            ('_self', _('Same window')),
            ('_blank', _('New window')),
        ],
        default='_self'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('url'),
                FieldPanel('title'),
                FieldPanel('target'),
            ]
        )
    ]



class BlogPage(BasePage):
    template = 'blog/blog_page.html'

    subpage_types = []
    parent_page_types = ['blog.BlogListingPage']

    is_use_case = models.BooleanField(default=False)
    short_description = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=1234)
    employees = ParentalManyToManyField('employees.Employee', blank=True)

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
        FieldPanel('is_use_case'),
        FieldPanel('likes'),
        MultiFieldPanel(
            [
                InlinePanel('links', label=_('Link'))
            ],
            heading=_('Links')
        ),
        MultiFieldPanel(
            [
                FieldPanel('employees', widget=forms.SelectMultiple)
            ],
            heading=_('Employees')
        ),
        StreamFieldPanel('content')
    ]

    @property
    def formatted_title(self):
        return '<h1 class="header__title">{}</h1>'.format(self.title)

    class Meta:
        verbose_name = 'Blog Page'
        verbose_name_plural = 'Blog Pages'
