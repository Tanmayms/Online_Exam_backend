# Generated by Django 4.1.3 on 2022-11-14 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_test_related_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.TextField(max_length=255)),
                ('option_a', models.CharField(max_length=100)),
                ('option_b', models.CharField(max_length=100)),
                ('option_c', models.CharField(max_length=100)),
                ('option_d', models.CharField(max_length=100)),
                ('correct_ans', models.CharField(max_length=100)),
                ('related_test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
            ],
        ),
    ]
