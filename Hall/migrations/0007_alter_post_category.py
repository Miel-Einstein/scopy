# Generated by Django 3.2.7 on 2021-09-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0006_auto_20210926_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='Category', null=True, on_delete=django.db.models.deletion.CASCADE, to='Hall.category'),
        ),
    ]
