# Generated by Django 3.2.7 on 2021-10-15 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0016_videos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
