# Generated by Django 4.0.3 on 2022-03-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_account_post_remove_post1_user_delete_account1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profileImage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
