# Generated by Django 4.2.14 on 2024-08-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0007_alter_user_email_alter_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]