# Generated by Django 2.1.4 on 2018-12-27 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('server', '0009_auto_20181226_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField()),
                ('session_key', models.CharField(blank=True, max_length=160, null=True)),
                ('authentication_key', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
