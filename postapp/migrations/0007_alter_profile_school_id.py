# Generated by Django 4.0.4 on 2022-07-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='school_id',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
