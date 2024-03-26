from django.shortcuts import render, redirect
from .forms import *


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listCategory")
    return render(request, "category/addCategory.html")


def add_book(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listBook")
    return render(request, "book/addBook.html", {"category": categories})


def list_category(request):
    category = Category.objects.all()
    return render(request, "category/listCategory.html", {"categories": category})


def list_books(request):
    books = Book.objects.all()
    return render(request, "book/listBook.html", {"books": books})