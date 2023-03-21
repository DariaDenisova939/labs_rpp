from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import TranslationParticipants, Bank, Card, Translation, Operations, PersonalData
from django.forms import ModelForm, TextInput


class TranslationParticipantsForm(ModelForm):
    class Meta:
        model = TranslationParticipants
        fields = ['name', 'surname', 'patronymic', 'phone_number', 'operation']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'}),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'}),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'}),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'}),
            "operation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Операция'}),
        }


class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'state_or_private', 'address']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название банка'}),
            "state_or_private": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Государственный или частный'}),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес главного офиса'}),
        }


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['participant_id', 'bank_id']
        widgets = {
            "participant_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Участника перевода'}),
            "bank_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Банка'}),
        }


class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields = ['device', 'participant_id', 'operation', 'number_type']
        widgets = {
            "device": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Устройство с которого выполнен перевод'}),
            "participant_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Участника перевода'}),
            "operation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Операция'}),
            "number_type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип номера по которому был совершен перевод'}),
        }


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = ['participant_id', 'passport_series', 'passport_number', 'division_code', 'place_of_residence']
        widgets = {
            "participant_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Участника перевода'}),
            "passport_series": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия паспорта'}),
            "passport_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер паспорта'}),
            "division_code": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код подразделения'}),
            "place_of_residence": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес регистрации'}),
        }


class OperationsForm(ModelForm):
    class Meta:
        model = Operations
        fields = ['participant_id', 'transfer_amount', 'currency', 'date', 'time', 'operation']
        widgets = {
            "participant_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Участника операции'}),
            "transfer_amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма'}),
            "currency": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Валюта'}),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата операции'}),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время операции'}),
            "operation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Операция'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-input'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-input'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
