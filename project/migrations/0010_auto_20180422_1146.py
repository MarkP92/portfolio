# Generated by Django 2.0.4 on 2018-04-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20180418_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.URLField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='project',
            name='website',
            field=models.URLField(default='', max_length=120),
        ),
    ]