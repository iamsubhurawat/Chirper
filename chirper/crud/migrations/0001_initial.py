# Generated by Django 5.1.2 on 2024-10-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.TextField(max_length=20)),
                ('age', models.IntegerField(max_length=2)),
                ('student_id', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('image', models.ImageField(height_field='50', upload_to='crud_images', width_field='50')),
                ('branch', models.TextField(max_length=20)),
            ],
        ),
    ]