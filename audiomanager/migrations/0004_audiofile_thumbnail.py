# Generated by Django 3.2.12 on 2023-05-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiomanager', '0003_auto_20230525_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
