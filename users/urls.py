from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('', login_request, name="login"),
    # path('signup/<str:name>', signup, name="REGISTER"),
    # path('', include('django.contrib.auth.urls'))
]
