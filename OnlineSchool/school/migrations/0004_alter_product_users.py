# Generated by Django 4.2.5 on 2023-09-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_product_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='buyers', to='school.user'),
        ),
    ]
