# Generated by Django 3.1.4 on 2021-01-19 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210119_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['publish_date', '-updated', '-timestamp']},
        ),
    ]
