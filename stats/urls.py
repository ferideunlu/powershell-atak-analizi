from django.urls import path
from . import views

urlpatterns = [
    path('view/<image>', views.view, name='view'),
]