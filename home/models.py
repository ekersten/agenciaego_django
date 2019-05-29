from django.db import models

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
