# Generated by Django 4.0.3 on 2022-03-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_alter_account_profileimage_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='account',
        ),
    ]