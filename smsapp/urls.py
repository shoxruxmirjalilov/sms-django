from django.urls import path
from . views import index
from smsapp import views

urlpatterns = [
    path('',views.index, name='index'),
]