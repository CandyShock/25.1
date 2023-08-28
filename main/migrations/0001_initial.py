# Generated by Django 4.2.4 on 2023-08-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='curse/', verbose_name='картинка')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='картинка')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
                ('url', models.URLField(max_length=50, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]