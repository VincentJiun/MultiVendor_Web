# Generated by Django 5.0.4 on 2024-07-16 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeprofile',
            old_name='store',
            new_name='user',
        ),
    ]
