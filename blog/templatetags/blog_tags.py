from django import template
from ..models import BlogPage

register = template.Library()

@register.simple_tag()
def latest_posts(ammount=10):
    return BlogPage.objects.live().public()[:ammount]


@register.simple_tag()
def blog_message():
    return 'Tengo {} posts'.format(BlogPage.objects.live().public().count())
