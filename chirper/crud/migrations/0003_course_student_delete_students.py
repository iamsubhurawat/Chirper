# Generated by Django 5.1.2 on 2024-10-30 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_students_age_alter_students_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.TextField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.TextField(max_length=20)),
                ('age', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(height_field='50', upload_to='crud_images', width_field='50')),
                ('course', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='crud.course')),
            ],
        ),
        migrations.DeleteModel(
            name='students',
        ),
    ]
