# Generated by Django 4.0.2 on 2022-03-25 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0022_rename_caterogy_furniture_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Handle',
        ),
        migrations.AlterModelOptions(
            name='calctag',
            options={'verbose_name': 'Тэг расчёта', 'verbose_name_plural': 'Тэги расчётов'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'verbose_name': 'Деталь', 'verbose_name_plural': 'Детали'},
        ),
    ]
