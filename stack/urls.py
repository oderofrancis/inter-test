from django.urls import path
from .views import *

urlpatterns = [
    path('api/messages/',MessageView.as_view()),
]