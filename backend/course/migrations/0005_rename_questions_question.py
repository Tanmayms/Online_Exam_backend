# Generated by Django 4.1.3 on 2022-11-14 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]