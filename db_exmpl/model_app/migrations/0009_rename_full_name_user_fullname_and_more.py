# Generated by Django 4.2.14 on 2024-08-01 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0008_alter_user_email_alter_user_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]