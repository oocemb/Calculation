# Generated by Django 4.0.2 on 2022-03-06 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0012_furniture_article_furniture_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnitureincalc',
            name='calc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calc.calc'),
            preserve_default=False,
        ),
    ]