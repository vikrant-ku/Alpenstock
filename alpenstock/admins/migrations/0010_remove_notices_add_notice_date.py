# Generated by Django 3.1.6 on 2021-02-24 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0009_auto_20210224_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notices',
            name='add_notice_date',
        ),
    ]
