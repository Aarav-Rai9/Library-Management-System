from django import forms
from .models import Category, Book, Student, LibraryCard


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'status']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'bookname', 'status', 'author', 'rating', 'cost']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade', 'library_card']


class LibraryCardForm(forms.ModelForm):
    class Meta:
        model = LibraryCard
        fields = ['student', 'book']
