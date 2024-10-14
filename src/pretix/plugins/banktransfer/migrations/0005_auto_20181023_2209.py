# Generated by Django 2.1 on 2018-10-23 22:09

from django.db import migrations


def set_type(app, schema_editor):
    EventSettingsStore = app.get_model('pretixbase', 'Event_SettingsStore')

    for setting in EventSettingsStore.objects.filter(key='payment_banktransfer_bank_details').select_related('object'):
        EventSettingsStore.objects.create(
            object=setting.object,
            key='payment_banktransfer_bank_details_type',
            value='other'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('banktransfer', '0004_auto_20170619_1125'),
    ]

    operations = [
        migrations.RunPython(set_type, migrations.RunPython.noop)
    ]
