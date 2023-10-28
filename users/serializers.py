from rest_framework import serializers

from courses.models import Course
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'education', 'profile_image', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')  # Remove password from validated_data
        user = User(**validated_data)
        user.set_password(password)  # Set the password separately
        user.save()
        return user
    
class AddCourseToEnrolledSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()  

    def validate_course_id(self, value):
        try:
            course = Course.objects.get(pk=value)
            return course
        except Course.DoesNotExist:
            raise serializers.ValidationError("Course with this ID does not exist.")

    def update(self, instance, validated_data):
        course = validated_data['course_id']
        if course not in instance.enrolled_courses.all():
            instance.enrolled_courses.add(course)
        return instance