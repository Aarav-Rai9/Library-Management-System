from django.shortcuts import render, redirect, get_object_or_404
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
        print(1)
        # category_id = request.POST.get("category")
        # category_object = get_category(category_id)
        form = BookForm(request.POST)
        # form.instance.category = category_object
        print(request.POST)
        if form.is_valid():
            print(2)
            form.save()
            return redirect("listBook")
    return render(request, "book/addBook.html", {"category": category})


def get_category(id):
    return get_object_or_404(Category, id=id)


def list_category(request):
    category = Category.objects.all()
    return render(request, "category/listCategory.html", {"categories": category})


def list_books(request):
    books = Book.objects.all()
    return render(request, "book/listBook.html", {"books": books})
