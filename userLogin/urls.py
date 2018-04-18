from django.urls import path
from . import views

app_name = 'userLogin'

urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login')
]