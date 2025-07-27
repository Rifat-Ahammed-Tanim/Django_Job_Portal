from django.urls import path
from users_auth_app.views import *

urlpatterns = [
    path('', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('dashboard/', dashboardPage, name='dashboard'),
]