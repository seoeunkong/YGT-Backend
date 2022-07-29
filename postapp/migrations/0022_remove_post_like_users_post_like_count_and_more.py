# Generated by Django 4.0.4 on 2022-07-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0021_alter_post_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_users',
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_post',
            field=models.ManyToManyField(blank=True, related_name='like_userss', to='postapp.post'),
        ),
    ]