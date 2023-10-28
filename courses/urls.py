
from django.urls import path
from .views import CourseList, CourseDetail

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    # path('courses/<int:pk>/signup/', UserSignupForCourse.as_view(), name='user-signup-for-course'),
]
