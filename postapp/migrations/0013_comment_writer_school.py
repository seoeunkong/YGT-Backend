# Generated by Django 4.0.4 on 2022-07-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0012_post_author_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writer_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postapp.profile'),
        ),
    ]
