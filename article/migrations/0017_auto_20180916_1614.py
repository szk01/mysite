# Generated by Django 2.1.1 on 2018-09-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20180916_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='article',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]
