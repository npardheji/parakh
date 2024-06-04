
from django.urls import path
from django.contrib.auth import views as auth_views
#from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.hello),
]
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)