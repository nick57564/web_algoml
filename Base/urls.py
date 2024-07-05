from django.urls import path
from .views import Base_view

urlpatterns=[
    path('', Base_view, name='Base_view'),
]