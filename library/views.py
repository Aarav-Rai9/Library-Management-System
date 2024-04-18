from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import *


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listCategory")
    return render(request, "category/addCategory.html")


def add_book(request):
    category = Category.objects.all()
    if request.method == "POST":
        category_id = request.POST.get("category")
        category_object = get_category(category_id)
        form = BookForm(request.POST)
        form.instance.category = category_object
        print(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("listBook")
            except Exception as e:
                return HttpResponseServerError(str(e))
        else:
            print(form.errors)
    return render(request, "book/addBook.html", {"category": category})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(f"id: {student.id}, name: {student.name}, grade: {student.grade}")
            library_card = LibraryCard.objects.create(student=student, issue_date=timezone.now())
            return render(request, "libraryCard/listLibraryCard.html", {"library_card": library_card})
        else:
            print(form.errors)
    return render(request, "student/addStudent.html")


def get_category(id):
    return get_object_or_404(Category, id=id)


def list_category(request):
    category = Category.objects.all()
    if request.method == "POST":
        categoryname = request.POST.get("search-category")
        if categoryname != "":
            category = Category.objects.filter(name__icontains=categoryname)
    return render(request, "category/listCategory.html", {"categories": category})


def list_books(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        bookname = request.POST.get("search-book")
        if bookname != "":
            books = Book.objects.filter(bookname__icontains=bookname)
    return render(request, "book/listBook.html", {"books": books, "categories": categories})
