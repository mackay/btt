from django.contrib import admin

from .models import Cause, Organization, Response

admin.site.register(Cause)
admin.site.register(Organization)
admin.site.register(Response)
