# Generated by Django 3.0.5 on 2020-04-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ursamajor', '0006_auto_20200428_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='translated',
            field=models.BooleanField(default=False),
        ),
    ]