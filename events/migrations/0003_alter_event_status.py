# Generated by Django 5.1.1 on 2024-11-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('open', '報名中'), ('closed', '報名截止'), ('not_open', '尚未開放報名')], default='not_open', max_length=20),
        ),
    ]
