from django.urls import path,include
from .views import helo
urlpatterns = [
    path('',helo)
]