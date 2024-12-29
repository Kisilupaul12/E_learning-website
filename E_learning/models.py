from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructors = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')
    progress = models.IntegerField(default=0)
    class Meta:
        unique_together = (('user', 'course'),)


    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'
