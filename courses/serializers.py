from rest_framework import serializers
from .models import Course, Program

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'format', 'mode', 'lessons', 'exams', 'literature', 'program')
        depth = 2
    def create(self, validated_data):
        # If you need to handle any additional logic during course creation, you can do it here
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # If you need to handle updating a course, you can do it here
        instance.title = validated_data.get('title', instance.title)
        instance.format = validated_data.get('format', instance.format)
        instance.mode = validated_data.get('mode', instance.mode)
        instance.lessons = validated_data.get('lessons', instance.lessons)
        instance.exams = validated_data.get('exams', instance.exams)
        instance.literature.set(validated_data.get('literature', instance.literature.all()))
        
        program_data = validated_data.get('program', {})
        if program_data:
            if instance.program:
                instance.program.content = program_data.get('content', instance.program.content)
                instance.program.save()
            else:
                Program.objects.create(course=instance, **program_data)
        
        instance.save()
        return instance
