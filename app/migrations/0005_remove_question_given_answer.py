# Generated by Django 3.2.9 on 2021-11-23 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_test_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='given_answer',
        ),
    ]