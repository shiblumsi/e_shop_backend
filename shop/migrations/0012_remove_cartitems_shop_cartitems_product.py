# Generated by Django 4.2.1 on 2023-05-07 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='shop',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
    ]
