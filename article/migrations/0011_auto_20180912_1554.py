# Generated by Django 2.1.1 on 2018-09-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20180910_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time']},
        ),
    ]