# Generated by Django 4.1.3 on 2023-04-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0007_articles_articlescategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='allprojects',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/ProjectsPDF'),
        ),
        migrations.AddField(
            model_name='articlescategory',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/ArticlesPDF'),
        ),
    ]
