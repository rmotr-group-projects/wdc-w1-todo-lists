from django.urls import path
from assignment_1.fixtures import views

urlpatterns = [path('', views.home, name='home')]