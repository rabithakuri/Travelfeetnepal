# Generated by Django 3.0.8 on 2020-07-13 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_feedback_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='Comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
