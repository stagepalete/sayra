from django.db import models

# Create your models here.
class StudyProgramm(models.Model):
    GRADE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('1 course', '1 course'),
        ('2 course', '2 course'),
        ('3 course', '3 course'),
        ('4 course', '4 course'),
    )
    SUBJECT_CHOICE = (
        ('Math', 'Math'),
        ('Physic', 'Physic'),
        ('Biology', 'Biology'),
        ('Geography', 'Geography'),
        ('English', 'English'),
    )
    INTEREST_CHOICE = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c')
    )
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICE)
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICE)
    description = models.TextField(default='')
    country = models.ForeignKey('programms.Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country
