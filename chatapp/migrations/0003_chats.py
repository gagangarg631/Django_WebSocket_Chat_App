# Generated by Django 4.0.1 on 2022-01-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_alter_notification_notify_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='deleted', max_length=50)),
                ('receiver', models.CharField(default='deleted', max_length=50)),
                ('message', models.TextField()),
                ('send_time', models.DateTimeField(auto_now=True)),
                ('receive_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
