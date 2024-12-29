from functools import reduce
from tokenize import generate_tokens

from .models import Course, Enrollment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import EnrollmentForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses_list.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the user from the form
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect to homepage or dashboard
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    else:
        form = AuthenticationForm()  # Create an empty form for GET requests

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('index')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})

# create a new course
@login_required
def course_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES.get('image', None)
        Course.objects.create(title=title, description=description, price=price, image=image, instructors=request.user)
        return redirect('course_Form')
    return render(request, 'courses_Form.html')

# Edit course
@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.price = request.POST['price']
        if 'image' in request.FILES:
            course.image = request.FILES['image']
        course.save()
        return redirect('course_list')
    return render(request, 'courses_list.html')


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
        if created:
            messages.success(request, f"You have successfully enrolled in {course.title}!")
        else:
            messages.info(request, f"You are already enrolled in {course.title}.")
        return redirect('enrolled_courses')  # Redirect to the enrolled courses page

    return render(request, 'enroll_course.html', {'course': course})



# def enroll_in_course(request, pk):
#     course = Course.objects.get(pk=pk)
#
#     if Enrollment.objects.filter(course=course).exists():
#         return redirect('course_detail', pk=course.pk)
#
#     enrollment = Enrollment(student=request.user, course=course)
#     enrollment.save()
#
#     return redirect('my_courses', pk=course.pk)
# views.py
@login_required
def enrolled_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    return render(request, 'enrolled_courses.html', {'enrollments': enrollments})


def dashboard(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'enrollments': enrollments})

def update_progress(user, course, progress_increment):
    enrollment = Enrollment.objects.get(user=user, course=course)
    enrollment.progress = min(100, enrollment.progress + progress_increment)
    enrollment.save()
