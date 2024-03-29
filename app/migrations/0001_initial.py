# Generated by Django 5.0.2 on 2024-02-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('gender', models.CharField(max_length=16, verbose_name='Пол')),
                ('username', models.CharField(max_length=128, verbose_name='Ник донора для фоток')),
                ('api_id', models.CharField(max_length=32, verbose_name='ID из инструментов разработчика')),
                ('api_hash', models.CharField(max_length=64, verbose_name='Hash из инструментов разработчика')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Был ли активирован')),
            ],
        ),
    ]
