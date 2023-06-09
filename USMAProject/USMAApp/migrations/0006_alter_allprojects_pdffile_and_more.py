# Generated by Django 4.1.3 on 2023-04-10 08:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0005_allprojects_github_allprojects_studentemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allprojects',
            name='PdfFile',
            field=models.CharField(blank=True, default='https://programmers.pythonanywhere.com/admin/DimosoApp/uploadfiles/32/change/pdfs/test_01__test_02.pdf', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='allprojects',
            name='ProjectBody',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='allprojects',
            name='VideoLink',
            field=models.CharField(blank=True, default='www.youtube.com/dimosojunior', max_length=200, null=True),
        ),
    ]
