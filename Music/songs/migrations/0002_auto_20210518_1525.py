# Generated by Django 3.2.3 on 2021-05-18 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='song_album',
        ),
        migrations.AlterField(
            model_name='album',
            name='upload',
            field=models.DateField(default=datetime.datetime(2021, 5, 18, 9, 55, 7, 7020, tzinfo=utc)),
        ),
    ]
