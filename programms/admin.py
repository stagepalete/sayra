from django.contrib import admin
from .models import StudyProgramm, Country
# Register your models here.
admin.site.register([StudyProgramm, Country])