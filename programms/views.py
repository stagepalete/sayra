from rest_framework import generics
from .models import StudyProgramm
from .serializers import StudyProgrammSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StudyProgrammList(generics.ListCreateAPIView):
    queryset = StudyProgramm.objects.all()
    serializer_class = StudyProgrammSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class StudyProgrammDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyProgramm.objects.all()
    serializer_class = StudyProgrammSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

