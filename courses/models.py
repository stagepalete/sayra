from django.db import models

class Course(models.Model):
    FORMAT_CHOICES = (
        ('group', 'Group'),
        ('indiv', 'Individual'),
    )
    MODE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=6, choices=FORMAT_CHOICES)
    mode = models.CharField(max_length=7, choices=MODE_CHOICES)
    lessons = models.PositiveIntegerField(default=0, help_text="Number of lessons")
    exams = models.BooleanField(default=False, help_text="Has exams")
    literature = models.ManyToManyField('Literature', blank=True)
    program = models.OneToOneField('Program', on_delete=models.SET_NULL, null=True, blank=True, related_name='course_program')
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Literature(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Program(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='course_program_reverse')
    content = models.TextField()
    
    def __str__(self):
        return f"Program for {self.course.title}"