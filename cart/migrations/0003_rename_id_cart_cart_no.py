# Generated by Django 4.0.4 on 2022-06-09 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='id',
            new_name='cart_no',
        ),
    ]
