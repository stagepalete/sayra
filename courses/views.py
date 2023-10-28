from django.shortcuts import render
from rest_framework import generics, status
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

# class UserSignupForCourse(generics.UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly,]

#     def update(self, request, *args, **kwargs):
#         course = self.get_object()
#         user = request.user

#         if course:
#             course.enrolled_students.add(user)
#             course.save()

#             return Response({'message': 'You are enrolled in the course'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Course format or mode not supported for enrollment'}, status=status.HTTP_400_BAD_REQUEST)