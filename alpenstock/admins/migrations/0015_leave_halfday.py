# Generated by Django 3.1.6 on 2021-03-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0014_leave_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='halfday',
            field=models.BooleanField(default=False),
        ),
    ]
