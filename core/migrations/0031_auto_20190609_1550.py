# Generated by Django 2.2.2 on 2019-06-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190609_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.ManyToManyField(related_name='quiz', to='core.Question'),
        ),
    ]