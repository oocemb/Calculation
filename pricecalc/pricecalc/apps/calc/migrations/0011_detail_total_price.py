# Generated by Django 4.0.2 on 2022-03-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_rename_widht_detail_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]