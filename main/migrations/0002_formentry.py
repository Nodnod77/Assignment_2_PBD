# Generated by Django 5.1.1 on 2024-09-17 17:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data1', models.CharField(max_length=255)),
                ('data2', models.DateField(auto_now_add=True)),
                ('data3', models.TextField()),
                ('data4', models.IntegerField()),
            ],
        ),
    ]
