# Generated by Django 2.0.4 on 2018-05-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tech', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='../media/img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('website', models.URLField(blank=True, default='', max_length=120, null=True)),
                ('github', models.URLField(blank=True, default='', max_length=120, null=True)),
                ('slug', models.SlugField(default='')),
            ],
            options={
                'verbose_name': 'Projekt',
                'verbose_name_plural': 'Projekter',
                'ordering': ['-created_at'],
            },
        ),
    ]
