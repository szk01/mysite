# Generated by Django 2.1.1 on 2018-09-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180908_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_type',
        ),
        migrations.DeleteModel(
            name='ArticleType',
        ),
    ]
