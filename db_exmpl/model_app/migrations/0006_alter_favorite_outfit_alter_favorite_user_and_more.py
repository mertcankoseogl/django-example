# Generated by Django 4.2.14 on 2024-07-31 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0005_alter_outfit_title_alter_favorite_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outfit_fav', to='model_app.outfit'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to='model_app.user'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_o', to='model_app.category'),
        ),
        migrations.AlterField(
            model_name='part',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outfit_part', to='model_app.outfit'),
        ),
    ]
