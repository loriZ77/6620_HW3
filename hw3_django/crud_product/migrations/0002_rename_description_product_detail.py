# Generated by Django 3.2.7 on 2021-10-06 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='detail',
        ),
    ]
