# Generated by Django 4.2.4 on 2024-02-16 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0022_alter_state_created_date_alter_state_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
        migrations.AlterField(
            model_name='state',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 29, 58, 253798)),
        ),
    ]