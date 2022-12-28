# Generated by Django 4.1.3 on 2022-11-15 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('article_text', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(verbose_name='Date Published')),
                ('date_updated', models.DateTimeField(verbose_name='Date Updated')),
                ('article_slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(verbose_name='Date Published')),
                ('author', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=500)),
                ('org', models.CharField(choices=[('CNN', 'CNN'), ('FOX', 'FOX'), ('NPR', 'NPR'), ('AP', 'AP'), ('MSNBC', 'MSNBC'), ('ABC', 'ABC'), ('CBS', 'CBS'), ('CNBC', 'CNBC'), ('NBC', 'NBC'), ('VICE', 'VICE'), ('BBC', 'BBC'), ('ESPN', 'ESPN'), ('other', 'Other')], default='other', max_length=10)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]