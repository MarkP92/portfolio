# Generated by Django 2.0.4 on 2018-05-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20180422_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tech',
            field=models.CharField(default='', max_length=150),
        ),
    ]