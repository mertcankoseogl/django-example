# Generated by Django 4.2.14 on 2024-08-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_user_photo_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='outfit_title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]
