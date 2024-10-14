# Generated by Django 3.2.4 on 2021-12-01 11:55

from django.db import migrations
from django.db.models import Count


def change_unique_identifiers(apps, schema_editor):
    # We cannot really know if a position was bundled or an add-on, but we can at least guess
    Question = apps.get_model("pretixbase", "Question")

    for r in Question.objects.values('event', 'identifier').order_by().annotate(c=Count('*')).filter(c__gt=1):
        qs = Question.objects.filter(identifier=r['identifier'], event_id=r['event'])
        for i, q in enumerate(qs[1:]):
            q.identifier += f'_{i + 2}'
            q.save(update_fields=['identifier'])


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0220_auto_20220811_1002'),
    ]

    operations = [
        migrations.RunPython(
            change_unique_identifiers,
            migrations.RunPython.noop,
        ),
    ]
