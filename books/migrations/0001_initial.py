# Generated by Django 5.1 on 2024-08-18 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_image', models.ImageField(upload_to='media/book_images')),
                ('title', models.CharField(max_length=250)),
                ('book_content', models.TextField()),
                ('description', models.TextField()),
                ('isbn_number', models.CharField(max_length=13, unique=True)),
                ('borrow_price', models.PositiveIntegerField()),
                ('stk_quantity', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField(default=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
                ('categories', models.ManyToManyField(to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='AddReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.book')),
            ],
        ),
    ]
