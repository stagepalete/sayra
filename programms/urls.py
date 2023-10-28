from django.urls import path
from .views import StudyProgrammList, StudyProgrammDetail

urlpatterns = [
    path('studyprograms/', StudyProgrammList.as_view(), name='studyprogramm-list'),
    path('studyprograms/<int:pk>/', StudyProgrammDetail.as_view(), name='studyprogramm-detail'),
]
