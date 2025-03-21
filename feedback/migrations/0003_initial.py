# Generated by Django 5.1.1 on 2024-12-09 16:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0002_remove_response_question_remove_registration_event_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('event_time', models.DateTimeField()),
                ('participants', models.ManyToManyField(related_name='feedback_checked_in_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
