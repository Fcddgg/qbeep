# Generated by Django 4.2.20 on 2025-04-12 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_registration_check_out_time_and_more'),
        ('feedback', '0015_alter_winner_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('question_type', models.CharField(choices=[('rating', '0-10 評分'), ('single_choice', '單選'), ('text', '文字回答')], max_length=20)),
                ('options', models.TextField(blank=True, help_text='選項用逗號分隔，例如：極佳, 相當好, 良好')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.form')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.response')),
            ],
        ),
    ]
