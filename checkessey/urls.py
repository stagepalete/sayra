
from django.urls import path
from .views import CheckEssey

urlpatterns = [
    path('check-essay/', CheckEssey.as_view(), name='check-essay'),
]