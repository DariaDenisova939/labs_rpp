from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from setuptools._entry_points import _


class TranslationParticipants(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    operation = models.CharField(max_length=30)

    def get_absolute_url(self):
        self
        return f'../trans_participants'


class Bank(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=30)
    state_or_private = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def get_absolute_url(self):
        self
        return f'../bank'


class Card(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    participant_id = models.ForeignKey(TranslationParticipants, on_delete=models.CASCADE)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def get_absolute_url(self):
        self
        return f'../card'


class Translation(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    device = models.CharField(max_length=30)
    participant_id = models.ForeignKey(TranslationParticipants, on_delete=models.CASCADE)
    operation = models.CharField(max_length=30)
    number_type = models.CharField(max_length=30)

    def get_absolute_url(self):
        self
        return f'../translation'


class PersonalData(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    participant_id = models.OneToOneField(TranslationParticipants, on_delete=models.CASCADE)
    passport_series = models.IntegerField()
    passport_number = models.IntegerField()
    division_code = models.IntegerField()
    place_of_residence = models.CharField(max_length=30)

    def get_absolute_url(self):
        self
        return f'../personal_data'


class Operations(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    participant_id = models.ForeignKey(TranslationParticipants, on_delete=models.CASCADE)
    transfer_amount = models.IntegerField()
    currency = models.CharField(max_length=30)
    date = models.DateField(_(u"Conversation Date"), blank=True)
    time = models.TimeField(_(u"Conversation Time"), blank=True)
    operation = models.CharField(max_length=30)

    def get_absolute_url(self):
        self
        return f'../operation'


class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title
