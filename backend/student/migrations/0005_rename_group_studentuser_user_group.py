# Generated by Django 4.1.3 on 2022-11-11 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='group',
            new_name='user_group',
        ),
    ]
