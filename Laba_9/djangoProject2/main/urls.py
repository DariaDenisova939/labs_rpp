from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path

from djangoProject2 import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('output/<int:idx>', views.output, name='output'),
    path('delete_check/<int:pk>/<int:idx>', views.delete_check, name='delete_check'),
    path('create/<int:idx>', views.create, name='create'),
    path('delete/<int:pk>/<int:idx>', views.delete, name='delete'),
    path('<int:pk>/update_participant', views.UpdateParticipants.as_view(), name='update_participant'),
    path('<int:pk>/update_bank', views.UpdateBank.as_view(), name='update_bank'),
    path('<int:pk>/update_card', views.UpdateCard.as_view(), name='update_card'),
    path('<int:pk>/update_operation', views.UpdateOperation.as_view(), name='update_operation'),
    path('<int:pk>/update_personal_data', views.UpdatePersonalData.as_view(), name='update_personal_data'),
    path('<int:pk>/update_translation', views.UpdateTranslation.as_view(), name='update_translation'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
