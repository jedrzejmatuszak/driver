# Generated by Django 2.2.2 on 2019-06-08 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190608_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='answer',
            new_name='answers',
        ),
    ]
