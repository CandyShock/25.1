# Generated by Django 4.2.4 on 2023-09-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_lesson_lesson_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_count',
        ),
    ]
