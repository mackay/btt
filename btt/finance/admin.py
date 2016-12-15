from django.contrib import admin

from .models import UserCause
from .models import CommitmentAllocation, Commitment
from .models import DonationPool, Donation

admin.site.register(UserCause)

admin.site.register(CommitmentAllocation)
admin.site.register(Commitment)

admin.site.register(DonationPool)
admin.site.register(Donation)
