from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.course_list, name='course_list'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.error_404, name='error_404'),
    path('login_view/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('courses/new/', views.course_create, name='course_Form'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_detail'),
    path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
     path('accounts/login/', views.login_view, name='login'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/enroll/', views.enroll_course, name='enroll'),
    path('enrolled_courses', views.enrolled_courses, name='enrolled_courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]