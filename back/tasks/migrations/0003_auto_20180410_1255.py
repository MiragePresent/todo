# Generated by Django 2.0 on 2018-04-10 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='from_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 10, 12, 55, 57, 517311)),
        ),
        migrations.AlterField(
            model_name='task',
            name='to_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]