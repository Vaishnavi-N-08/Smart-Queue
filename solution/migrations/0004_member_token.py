# Generated by Django 3.2.8 on 2022-02-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0003_auto_20220201_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='token',
            field=models.IntegerField(default=0),
        ),
    ]
