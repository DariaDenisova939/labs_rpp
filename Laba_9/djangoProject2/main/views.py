from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TranslationParticipants
from .models import Card
from .models import Bank
from .models import Translation
from .models import PersonalData
from .models import Operations
from .forms import TranslationParticipantsForm, CardForm, OperationsForm, PersonalDataForm, TranslationForm, \
    RegisterUserForm, LoginUserForm
from .forms import BankForm
from django.views.generic import UpdateView, CreateView


def index(request):
    return render(request, 'main/index.html', {'role': get_role(request.user)})


def output(request, idx):
    paths = ['TranslationParticipants/trans_participants.html', 'Card/card.html', 'Operations/operations.html',
             'PersonalData/personal_data.html', 'Translations/translation.html', 'Bank/bank.html']
    models = [TranslationParticipants, Card, Operations, PersonalData, Translation, Bank]
    attributes = models[idx].objects.all()
    return render(request, 'main/' + paths[idx],
                  {'attributes': attributes, 'role': get_role(request.user)})


class UpdateParticipants(UpdateView):
    model = TranslationParticipants
    template_name = 'main/TranslationParticipants/create.html'
    form_class = TranslationParticipantsForm
    success_url = '/output/0'


def delete(request, idx, pk):
    models = [TranslationParticipants, Card, Operations, PersonalData, Translation, Bank]
    paths = ['TranslationParticipants/trans_participants.html', 'Card/card.html', 'Operations/operations.html',
             'PersonalData/personal_data.html', 'Translations/translation.html', 'Bank/bank.html']
    obj = models[idx].objects.get(id=pk)
    obj.delete()
    attributes = models[idx].objects.all()
    return render(request, 'main/' + paths[idx], {'attributes': attributes, 'role': get_role(request.user)})


def delete_check(request, idx, pk):
    data = {
        'idx_tmp': idx,
        'pk_tmp': pk
    }
    return render(request, 'main/delete-entry.html', data)


def create(request, idx):
    paths = ['TranslationParticipants/create.html', 'Card/create_card.html', 'Operations/create_operation.html',
             'PersonalData/create_personal_data.html', 'Translations/create_translation.html', 'Bank/create_bank.html']
    forms = [TranslationParticipantsForm, CardForm, OperationsForm, PersonalDataForm, TranslationForm, BankForm]
    error = ''
    if request.method == 'POST':
        form = forms[idx](request.POST)
        if form.is_valid():
            form.save()
        else:
            error = form.errors.get_json_data(escape_html=False)
    form = forms[idx]()
    data = {
        'form': form,
        'error': error,
        'role': get_role(request.user)
    }
    return render(request, 'main/' + paths[idx], data)


class UpdateBank(UpdateView):
    model = Bank
    template_name = 'main/Bank/create_bank.html'
    form_class = BankForm
    success_url = '/output/5'


class UpdateCard(UpdateView):
    model = Card
    template_name = 'main/Card/create_card.html'
    form_class = CardForm
    success_url = '/output/1'


class UpdateOperation(UpdateView):
    model = Operations
    template_name = 'main/Operations/create_operation.html'
    form_class = OperationsForm
    success_url = '/output/2'


class UpdatePersonalData(UpdateView):
    model = PersonalData
    template_name = 'main/PersonalData/create_personal_data.html'
    form_class = PersonalDataForm
    success_url = '/output/3'


class UpdateTranslation(UpdateView):
    model = Translation
    template_name = 'main/Translations/create_translation.html'
    form_class = TranslationForm
    success_url = '/output/4'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def get_role(user):
    template = ""
    if user.is_authenticated:
        if user.is_superuser:
            template = "Admin"
        elif user.username == 'Teller':
            template = "Teller"
        else:
            template = "User"
    return template
