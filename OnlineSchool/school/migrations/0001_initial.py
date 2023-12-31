# Generated by Django 4.2.5 on 2023-09-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('video_url', models.URLField()),
                ('video_length', models.TimeField()),
                ('products', models.ManyToManyField(to='school.product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserTutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_time', models.TimeField(default=0)),
                ('watch_status', models.BinaryField(default=False)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.tutorial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.user')),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='users',
            field=models.ManyToManyField(through='school.UserTutorial', to='school.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='school.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(related_name='buyers', to='school.user'),
        ),
    ]
