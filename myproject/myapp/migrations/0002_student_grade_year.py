# Generated by Django 5.1.4 on 2025-01-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade_year',
            field=models.CharField(default='Waiting', max_length=50),
        ),
    ]