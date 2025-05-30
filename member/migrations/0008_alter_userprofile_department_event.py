# Generated by Django 5.1.1 on 2024-12-09 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_alter_userprofile_phone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, default='未指定', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('event_time', models.DateTimeField()),
                ('participants', models.ManyToManyField(related_name='checked_in_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
