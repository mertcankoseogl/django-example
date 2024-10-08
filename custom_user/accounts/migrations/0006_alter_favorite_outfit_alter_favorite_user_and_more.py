# Generated by Django 4.2.14 on 2024-08-08 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_part_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outfit_favorite', to='accounts.outfit'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_outfit', to='accounts.category'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_outfit', to=settings.AUTH_USER_MODEL),
        ),
    ]
