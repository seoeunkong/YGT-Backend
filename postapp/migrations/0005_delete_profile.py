# Generated by Django 4.0.4 on 2022-07-28 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_alter_profile_school_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]