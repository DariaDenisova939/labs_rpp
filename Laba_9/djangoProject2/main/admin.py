from django.contrib import admin
from .models import Operations
from .models import PersonalData
from .models import Translation
from .models import Card
from .models import Bank
from .models import TranslationParticipants
admin.site.register(Operations)
admin.site.register(Translation)
admin.site.register(PersonalData)
admin.site.register(Card)
admin.site.register(Bank)
admin.site.register(TranslationParticipants)