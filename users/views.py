from django.shortcuts import render
from courses.models import Course

from users.permissions import IsOwnerOrReadOnly
from .models import User
from .serializers import AddCourseToEnrolledSerializer, UserSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Issue a token for the new user (if using token authentication)
            from rest_framework.authtoken.models import Token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddCourseToEnrolled(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AddCourseToEnrolledSerializer

    def update(self, request, *args, **kwargs):
        course_id = self.kwargs.get('course_id')
        user = self.request.user

        if user.is_authenticated:
            try:
                course = Course.objects.get(pk=course_id)
                if course not in user.enrolled_courses.all():
                    user.enrolled_courses.add(course)
                    user.save()
                    return Response({'message': 'Course added to enrolled courses'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Course is already in enrolled courses'}, status=status.HTTP_400_BAD_REQUEST)
            except Course.DoesNotExist:
                return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)