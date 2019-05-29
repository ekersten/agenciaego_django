from django.utils.translation import ugettext as _
from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock
class PageBlock(blocks.StructBlock):
    page = PageChooserBlock()
    
    class Meta:
        template = 'home/blocks/page_block.html'
        icon = 'site'
        label = _('Featured Page')


class ThreePagesBlock(blocks.StructBlock):
    title = blocks.TextBlock(default='Publicaciones destacadas')

    page1 = PageChooserBlock()
    page2 = PageChooserBlock()
    page3 = PageChooserBlock()

    class Meta:
        template = 'home/blocks/featured_pages.html'
        icon = 'placeholder'
        label = _('Featured Pages')
