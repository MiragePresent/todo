# Generated by Django 2.0 on 2018-04-11 12:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20180411_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(default=datetime.datetime(2018, 4, 11, 12, 6, 4, 762668))),
                ('stopped_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='from_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 12, 6, 4, 749970)),
        ),
        migrations.AddField(
            model_name='taskactivity',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
