"""
URL configuration for Library_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addCategory/', views.add_category, name='addCategory'),
    path('addBook/', views.add_book, name='addBook'),
    path('listCategory/', views.list_category, name='listCategory'),
    path('listBook/', views.list_books, name='listBook'),
    path('addStudent/', views.add_student, name='addStudent'),
    path('listStudent/', views.list_students, name='listStudent'),
    path('editBook/<int:book_id>/', views.edit_book, name='editBook'),
    path('editCategory/<int:category_id>/', views.edit_category, name='editCategory'),
    path('deleteCategory/<int:category_id>/', views.delete_category, name='deleteCategory'),
    path('editStudent/<int:student_id>/', views.edit_student, name='editStudent'),
    path('assignBook/', views.assign_book, name='assignBook')
]
