# Generated by Django 4.0.2 on 2022-03-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_remove_detail_material_remove_detail_specdetail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='width',
            new_name='width',
        ),
    ]
