# Generated by Django 3.1.6 on 2021-02-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_auto_20210218_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student'),
        ),
    ]
