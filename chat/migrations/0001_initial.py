# Generated by Django 5.0.4 on 2024-04-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatMsg',
            fields=[
                ('sender', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
