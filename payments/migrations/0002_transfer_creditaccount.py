# Generated by Django 3.2.6 on 2021-11-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='CreditAccount',
            field=models.CharField(default=None, max_length=225),
            preserve_default=False,
        ),
    ]
