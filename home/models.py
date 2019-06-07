from django.db import models
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from .blocks import PageBlock, ThreePagesBlock


class HomePage(Page):
    template = 'home/home.html'

    content = StreamField(
        [
            ('page', PageBlock()),
            ('three_pages', ThreePagesBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key('home_page', [self.id])
        cache.delete(key)
        return super().save(*args, **kwargs)
