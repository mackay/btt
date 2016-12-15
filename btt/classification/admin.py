from django.contrib import admin

from .models import TwitterAccount, Tweet
from .models import Classification, ClassificationCause, ClassificationMeta

admin.site.register(TwitterAccount)
admin.site.register(Tweet)

admin.site.register(Classification)
admin.site.register(ClassificationCause)
admin.site.register(ClassificationMeta)
