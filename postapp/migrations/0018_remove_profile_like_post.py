# Generated by Django 4.0.4 on 2022-07-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0017_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='like_post',
        ),
    ]