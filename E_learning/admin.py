from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructors', 'description', 'price', 'created_at')
    search_fields = ('title', 'description')