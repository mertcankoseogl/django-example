# Generated by Django 4.2.14 on 2024-08-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_category_title_alter_outfit_outfit_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='outfit_title',
            field=models.CharField(max_length=100),
        ),
    ]
