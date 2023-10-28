from rest_framework import serializers
from .models import StudyProgramm

class StudyProgrammSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgramm
        fields = '__all__'
        depth = 2

