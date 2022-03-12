# Generated by Django 4.0.3 on 2022-03-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profileImage',
        ),
        migrations.AddField(
            model_name='post',
            name='follower',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='userID',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]