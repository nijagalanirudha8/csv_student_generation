# Generated by Django 5.0.7 on 2024-07-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('usn', models.CharField(max_length=20, unique=True)),
                ('course', models.CharField(choices=[('PY', 'Python'), ('MA', 'Mathematics'), ('JV', 'Java'), ('RB', 'Ruby'), ('BT', 'Biotechnology'), ('MBA', 'MBA')], max_length=10)),
            ],
        ),
    ]
