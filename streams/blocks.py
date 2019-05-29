from django.utils.translation import ugettext as _
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)

    class Meta:
        template = 'streams/title_block.html'
        icon = 'title'
        label = _('Main Title')
        group = _('Text')


class SubtitleBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=True)

    class Meta:
        template = 'streams/subtitle_block.html'
        icon = 'title'
        label = _('Subtitle')
        group = _('Text')


class SimpleRichTextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'ul',
            'link'
        ]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = _('Simple RichText')
        group = _('Text')


class BlockQuoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=True)

    class Meta:
        template = 'streams/blockquote_block.html'
        icon = 'openquote'
        label = _('Block Quote')
        group = _('Text')


class YoutubeEmbedBlock(blocks.StructBlock):
    youtube_video_id = blocks.CharBlock(required=True, help_text=_(
        'What goes after the "v=" in the url. Ex.: d9_DByee4FE '))

    class Meta:
        template = 'streams/youtube_embed_block.html'
        icon = 'media'
        label = _('Youtube Video')
        group = _('Media')


class FullWidthImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text=_('Suggested width 1920px'))
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = 'streams/full_width_image_block.html'
        icon = 'image'
        label = _('Full Width Image')
        group = _('Media')


class TextImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text=_('Suggested width 1200px'))
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = 'streams/text_image_block.html'
        icon = 'image'
        label = _('Text Image')
        group = _('Media')


class TitleImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text=_('Suggested width 1200px'))
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = 'streams/title_image_block.html'
        icon = 'image'
        label = _('Title Image')
        group = _('Media')
