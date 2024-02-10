# Generated by Django 4.2.4 on 2024-02-10 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0009_alter_state_created_date_alter_state_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 921072)),
        ),
        migrations.AlterField(
            model_name='state',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 921072)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 925080)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 925080)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 922081)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 18, 22, 49, 922081)),
        ),
    ]
