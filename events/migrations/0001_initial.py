# Generated by Django 5.1.1 on 2024-10-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('capacity_limit', models.PositiveIntegerField()),
                ('registration_start', models.DateTimeField()),
                ('registration_end', models.DateTimeField()),
                ('activity_type', models.CharField(choices=[('lecture', '講座'), ('seminar', '研討會')], max_length=20)),
                ('status', models.CharField(choices=[('open', '報名中'), ('closed', '報名截止'), ('not_open', '尚未開放報名')], max_length=20)),
                ('published_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]