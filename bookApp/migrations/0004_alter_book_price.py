# Generated by Django 4.2.3 on 2024-08-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0003_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
