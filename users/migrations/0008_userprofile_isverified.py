# Generated by Django 4.1.5 on 2023-03-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userprofile_categories_userprofile_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
    ]
