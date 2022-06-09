# Generated by Django 4.0.4 on 2022-06-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_order_total_payment_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('S', 'Shipped'), ('D', 'Delivered')], default='P', max_length=1),
        ),
    ]
