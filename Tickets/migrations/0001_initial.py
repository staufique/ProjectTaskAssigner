# Generated by Django 4.2.4 on 2024-02-10 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=200)),
                ('state_code', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 2, 10, 10, 43, 46, 251483))),
                ('updated_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('joining_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 2, 10, 10, 43, 46, 252488))),
                ('updated_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Tickets.state')),
            ],
        ),
        migrations.CreateModel(
            name='TaskMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('assign_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 2, 10, 10, 43, 46, 254486))),
                ('updated_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Tickets.state')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.usermaster')),
            ],
        ),
    ]
