# Generated by Django 4.2.14 on 2024-07-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0004_auto_20240729_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'outfit')},
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('follower', 'followed')},
        ),
    ]