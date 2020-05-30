# Generated by Django 3.0 on 2020-01-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beaconasset',
            options={'ordering': ['last_name']},
        ),
        migrations.RenameField(
            model_name='beaconasset',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='beaconasset',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]