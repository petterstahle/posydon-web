# Generated by Django 3.0.4 on 2020-04-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0006_simprop'),
    ]

    operations = [
        migrations.AddField(
            model_name='simprop',
            name='step_end',
            field=models.CharField(blank=True, default='end', max_length=20),
        ),
    ]
