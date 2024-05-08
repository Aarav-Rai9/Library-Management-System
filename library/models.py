from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="1")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.books.all().delete()
        super().delete(*args, **kwargs)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    author = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    cost = models.FloatField()
    description = models.TextField(default='')

    def __str__(self):
        return self.bookname


class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)


class LibraryCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name='library_card')
    issue_date = models.DateTimeField()

