# Generated by Django 2.2.2 on 2019-06-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20190609_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='for_hint',
            field=models.TextField(null=True),
        ),
    ]
