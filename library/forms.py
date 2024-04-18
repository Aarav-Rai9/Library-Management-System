from django import forms
from .models import Category, Book, Student, LibraryCard


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'status']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'bookname', 'status', 'author', 'rating', 'cost', 'description']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade']


class LibraryCardForm(forms.ModelForm):
    class Meta:
        model = LibraryCard
        fields = ['student', 'book', 'issue_date']
