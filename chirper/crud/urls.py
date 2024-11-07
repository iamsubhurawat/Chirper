from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_home, name='crud_home'),
    path('create_student/', views.create_student, name='crud_create_student'),
    path('create_course/', views.create_course, name='crud_create_course'),
    path('search_student/', views.search_student, name='crud_search_student'),
    path('view_student/', views.view_student, name='crud_view_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
] 