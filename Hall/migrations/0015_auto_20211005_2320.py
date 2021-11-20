# Generated by Django 3.2.7 on 2021-10-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0014_alter_videos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='image',
        ),
        migrations.AlterField(
            model_name='videos',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='static/video'),
        ),
    ]
