# Generated by Django 4.0.4 on 2022-05-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_alter_coupon_valid_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(),
        ),
    ]
