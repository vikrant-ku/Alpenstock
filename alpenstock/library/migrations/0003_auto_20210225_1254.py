# Generated by Django 3.1.6 on 2021-02-25 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_issue_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue_book',
            old_name='user',
            new_name='username',
        ),
    ]
