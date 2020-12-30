from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('index/', index, name="index"),
    # path('login/', login, name="login"),
    # path('signup/<str:name>', signup, name="REGISTER"),
    # path('', include('django.contrib.auth.urls'))
]
