# Generated by Django 4.1.3 on 2023-03-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0002_teachers_students_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='Year',
            field=models.CharField(blank=True, default='First Year', max_length=100, null=True),
        ),
    ]
