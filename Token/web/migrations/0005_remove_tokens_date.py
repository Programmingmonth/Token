# Generated by Django 5.0.6 on 2024-05-20 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_tokens_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokens',
            name='date',
        ),
    ]
