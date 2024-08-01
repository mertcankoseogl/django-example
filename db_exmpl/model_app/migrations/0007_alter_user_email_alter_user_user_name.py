# Generated by Django 4.2.14 on 2024-08-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0006_alter_favorite_outfit_alter_favorite_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='default user', max_length=50, unique=True),
        ),
    ]
