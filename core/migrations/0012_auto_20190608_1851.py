# Generated by Django 2.2.2 on 2019-06-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190608_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Hint'),
        ),
    ]
