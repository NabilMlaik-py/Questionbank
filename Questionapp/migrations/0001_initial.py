# Generated by Django 3.0 on 2019-12-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='q_a',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=255)),
                ('Answer1', models.CharField(max_length=255)),
                ('Answer2', models.CharField(max_length=255)),
                ('Answer3', models.CharField(max_length=255)),
                ('Answer4', models.CharField(max_length=255)),
                ('CorAns', models.CharField(max_length=255)),
            ],
        ),
    ]
