# Generated by Django 4.2.4 on 2024-02-16 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0020_alter_state_created_date_alter_state_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 27, 33, 196226)),
        ),
        migrations.AlterField(
            model_name='state',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 27, 33, 196226)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 27, 33, 199247)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 22, 27, 33, 199247)),
        ),
    ]
