# Generated by Django 3.0.3 on 2020-07-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20200625_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='Country',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
