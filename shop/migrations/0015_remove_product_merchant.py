# Generated by Django 4.2.1 on 2023-05-08 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_connection_shop_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='merchant',
        ),
    ]
