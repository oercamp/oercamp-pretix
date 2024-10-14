# Generated by Django 2.1.5 on 2019-01-18 15:27
from django.db import migrations


def enable_notifications_for_everyone(apps, schema_editor):
    NotificationSetting = apps.get_model('pretixbase', 'NotificationSetting')
    User = apps.get_model('pretixbase', 'User')
    create = []
    for u in User.objects.iterator():
        create.append(NotificationSetting(
            user=u,
            action_type='pretix.event.order.refund.requested',
            event=None,
            method='mail',
            enabled=True
        ))
        if len(create) > 200:
            NotificationSetting.objects.bulk_create(create)
            create.clear()
    NotificationSetting.objects.bulk_create(create)
    create.clear()


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0105_auto_20190112_1512'),
    ]

    operations = [
        migrations.RunPython(enable_notifications_for_everyone, migrations.RunPython.noop)
    ]
