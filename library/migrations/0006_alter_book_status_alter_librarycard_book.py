# Generated by Django 5.0.1 on 2024-05-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='librarycard',
            name='book',
            field=models.ManyToManyField(related_name='library_card', to='library.book'),
        ),
    ]
