# Generated by Django 4.2.16 on 2024-12-04 14:50

from django.db import migrations, models
import pretix.base.models.orders


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0278_remove_item_addon_item_dependency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pretalx_secret_token',
            field=models.CharField(default=pretix.base.models.orders.generate_secret, max_length=32),
        ),
    ]
