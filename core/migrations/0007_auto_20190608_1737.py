# Generated by Django 2.2.2 on 2019-06-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190608_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(null=True, to='core.Answer'),
        ),
    ]
