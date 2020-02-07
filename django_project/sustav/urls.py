from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Sustav-Početna"),
    path('students/', views.students, name="Sustav-Students"),
    path('courses/', views.courses, name="Sustav-Courses"),
    path('predmet/<predmet>/', views.predmet, name="predmet"),
    path('predmetEdit/<predmet>/', views.predmetEdit, name="predmetEdit"),
    path('studentEdit/<korisnik>/', views.studentEdit, name="studentEdit"),
    path('upisniList/<korisnik>/', views.upisniList, name="upisniList"),
    path('add/<int:pk>/<int:cpk>/', views.add, name="add"),
    path('remove/<int:pk>/<int:cpk>/', views.remove, name="remove"),
    path('passed/<int:pk>/<int:cpk>/', views.passed, name="passed"),
]