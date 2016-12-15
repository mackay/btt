from django.contrib import admin

from .models import Campaign, EngagementPurpose, Engagement

admin.site.register(Campaign)
admin.site.register(EngagementPurpose)
admin.site.register(Engagement)
