# Generated by Django 4.2.5 on 2023-09-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_usertutorial_watch_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='video_length',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usertutorial',
            name='watch_time',
            field=models.IntegerField(default=0),
        ),
    ]
