from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting,register_setting

@register_setting
class AgenciaEgoSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text='Facebook URL')
    twitter = models.URLField(blank=True, null=True, help_text='Twitter URL')
    instagram = models.URLField(blank=True, null=True, help_text='Instagram URL')
    linkedin = models.URLField(blank=True, null=True, help_text='LinkedIn URL')
    behance = models.URLField(blank=True, null=True, help_text='Behance URL')
    google_analytics_id = models.CharField(max_length=100, blank=True, null=True, help_text='Google Analytics ID')
    google_tagmanager_id = models.CharField(max_length=100, blank=True, null=True, help_text='Google TagManager ID')

    panels = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('instagram'),
            FieldPanel('linkedin'),
            FieldPanel('behance'),
        ], heading='Social Media Settings'),
        MultiFieldPanel([
            FieldPanel('google_analytics_id'),
            FieldPanel('google_tagmanager_id'),
        ], heading='Google Tracking IDs')
    ]
