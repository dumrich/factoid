# Generated by Django 4.1.4 on 2022-12-29 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_article_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Source',
        ),
    ]
