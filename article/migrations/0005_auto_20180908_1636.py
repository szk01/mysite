# Generated by Django 2.1.1 on 2018-09-08 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
