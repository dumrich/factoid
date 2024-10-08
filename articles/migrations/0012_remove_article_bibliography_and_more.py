# Generated by Django 4.1.5 on 2023-03-12 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='bibliography',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceFive',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceFiveOrg',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceFour',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceFourOrg',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceOne',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceOneOrg',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceThree',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceThreeOrg',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceTwo',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sourceTwoOrg',
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(blank=True, max_length=300, null=True)),
                ('sourceOrg', models.CharField(blank=True, choices=[('CNN', 'CNN'), ('FOX', 'FOX'), ('NPR', 'NPR'), ('AP', 'AP'), ('MSNBC', 'MSNBC'), ('ABC', 'ABC'), ('CBS', 'CBS'), ('CNBC', 'CNBC'), ('NBC', 'NBC'), ('VICE', 'VICE'), ('BBC', 'BBC'), ('ESPN', 'ESPN'), ('other', 'Other')], default='other', max_length=10, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
