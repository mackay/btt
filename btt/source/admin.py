from django.contrib import admin

from .models import Account, Tweet
from .models import Classification, ClassificationCause, ClassificationMeta

admin.site.register(Account)
admin.site.register(Tweet)

admin.site.register(Classification)
admin.site.register(ClassificationCause)
admin.site.register(ClassificationMeta)
