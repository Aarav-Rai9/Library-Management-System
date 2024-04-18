from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="1")


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField()
    cost = models.FloatField()
    description = models.TextField(default='')


class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)


class LibraryCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    issue_date = models.DateTimeField()

