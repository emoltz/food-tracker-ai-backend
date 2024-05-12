# Generated by Django 5.0.3 on 2024-05-12 00:39

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('sugars', models.FloatField()),
                ('food_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='New Meal', max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_display', models.CharField(max_length=100)),
                ('image_name', models.CharField(default='defaultImage', max_length=255)),
                ('composite_description', models.TextField(blank=True)),
                ('user_description', models.TextField(blank=True)),
                ('food_items', models.ManyToManyField(blank=True, to='api.food')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('meals', models.ManyToManyField(blank=True, to='api.meal')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.ManyToManyField(blank=True, to='api.day')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
