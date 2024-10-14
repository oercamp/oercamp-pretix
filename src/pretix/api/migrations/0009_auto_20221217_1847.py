# Generated by Django 3.2.16 on 2022-12-17 18:47

import uuid

import django.db.models.deletion
import oauth2_provider.generators
import oauth2_provider.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0226_itemvariationmetavalue'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pretixapi', '0008_webhookcallretry'),
    ]
    run_before = [
        ('oauth2_provider', '0002_auto_20190406_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauthapplication',
            name='algorithm',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='oauthgrant',
            name='claims',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oauthgrant',
            name='code_challenge',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='oauthgrant',
            name='code_challenge_method',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='oauthgrant',
            name='nonce',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='oauthapplication',
            name='client_secret',
            field=oauth2_provider.models.ClientSecretField(db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255),
        ),
        migrations.CreateModel(
            name='OAuthIDToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('jti', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('organizers', models.ManyToManyField(to='pretixbase.Organizer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pretixapi_oauthidtoken', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='oauthaccesstoken',
            name='id_token',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='access_token', to='pretixapi.oauthidtoken'),
        ),
    ]
