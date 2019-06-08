# Generated by Django 2.2.2 on 2019-06-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190608_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_answer', models.TextField()),
                ('negative_answer1', models.TextField()),
                ('negative_answer2', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Answer'),
        ),
    ]
