# Generated by Django 4.2.14 on 2024-08-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_outfit_is_kid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='subtitle',
            field=models.CharField(max_length=50),
        ),
    ]
