# Generated by Django 4.2.10 on 2024-05-14 10:30

from django.db import migrations


def use_sales_channels(apps, schema_editor):
    SalesChannel = apps.get_model("pretixbase", "SalesChannel")
    TicketLayoutItem = apps.get_model("ticketoutputpdf", "TicketLayoutItem")
    for sc in SalesChannel.objects.all():
        TicketLayoutItem.objects.filter(item__event__organizer_id=sc.organizer_id, sales_channel_type=sc.identifier).update(
            sales_channel=sc
        )


class Migration(migrations.Migration):
    dependencies = [
        ("ticketoutputpdf", "0009_sales_channels_new_fields"),
    ]

    operations = [
        migrations.RunPython(use_sales_channels, migrations.RunPython.noop),
    ]
