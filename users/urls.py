
from django.urls import path
from .views import AddCourseToEnrolled, UserList, UserDetail, UserLogin, UserSignup

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('users/enroll/<int:course_id>/', AddCourseToEnrolled.as_view(), name='enroll-course'),
]
