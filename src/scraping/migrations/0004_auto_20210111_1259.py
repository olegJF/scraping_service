# Generated by Django 3.1.5 on 2021-01-11 12:59

from django.db import migrations, models
import django.db.models.deletion
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='error',
            name='data',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_data',
            field=models.JSONField(default=scraping.models.default_urls),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='scraping.city', verbose_name='Город'),
        ),
    ]