# Generated by Django 5.1.1 on 2024-09-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_formentry_data2_alter_formentry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formentry',
            name='time',
        ),
        migrations.AlterField(
            model_name='formentry',
            name='data2',
            field=models.TextField(),
        ),
    ]
