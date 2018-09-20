# Generated by Django 2.1.1 on 2018-09-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
