from django.contrib import admin

from .models import Cause, Organization, EngagementContent

admin.site.register(Cause)
admin.site.register(Organization)
admin.site.register(EngagementContent)
