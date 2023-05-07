# Generated by Django 4.2.1 on 2023-05-07 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
