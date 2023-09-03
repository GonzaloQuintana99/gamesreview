from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_form, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name="authmanager/logout.html"), name="logout"),
    path('profile/', editProfile, name="editProfile"),
    path('creators/', users, name="creators"),
]