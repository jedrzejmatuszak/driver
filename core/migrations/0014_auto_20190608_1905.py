# Generated by Django 2.2.2 on 2019-06-08 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190608_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='hint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quiz', to='core.Hint'),
        ),
    ]
