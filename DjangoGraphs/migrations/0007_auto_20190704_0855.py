# Generated by Django 2.2.3 on 2019-07-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoGraphs', '0006_auto_20190704_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='active',
        ),
        migrations.AddField(
            model_name='graph',
            name='dashboard',
            field=models.BooleanField(default=False),
        ),
    ]