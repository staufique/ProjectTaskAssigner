# Generated by Django 4.2.4 on 2024-02-10 09:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0002_alter_state_created_date_alter_state_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 278928)),
        ),
        migrations.AlterField(
            model_name='state',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 278928)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 285479)),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.state'),
        ),
        migrations.AlterField(
            model_name='taskmaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 285479)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 278928)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.state'),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 56, 30, 278928)),
        ),
    ]
