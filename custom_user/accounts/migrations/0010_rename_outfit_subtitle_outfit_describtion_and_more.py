# Generated by Django 4.2.14 on 2024-08-09 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_outfit_outfit_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outfit',
            old_name='outfit_subtitle',
            new_name='describtion',
        ),
        migrations.RemoveField(
            model_name='part',
            name='subtitle',
        ),
    ]
