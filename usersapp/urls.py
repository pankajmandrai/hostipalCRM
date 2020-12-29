from django.urls import path, include
from .views import index, login, signup

urlpatterns = [
    path('', index, name="home"),
    path('login/', login, name="login"),
    path('signup/<str:name>', signup, name="REGISTER"),
    path('', include('django.contrib.auth.urls'))
]
