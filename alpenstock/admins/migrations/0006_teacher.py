# Generated by Django 3.1.6 on 2021-02-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_auto_20210220_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='ST', max_length=20)),
                ('password', models.CharField(default='', max_length=500)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('gender', models.CharField(default='', max_length=6)),
                ('dob', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('country', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('zipcode', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('designation', models.CharField(default='', max_length=20)),
                ('qualification', models.CharField(default='', max_length=30)),
                ('basic_salary', models.CharField(default='', max_length=30)),
                ('contract_type', models.CharField(default='', max_length=30)),
                ('work_shift', models.CharField(default='', max_length=30)),
                ('bank_name', models.CharField(default='', max_length=20)),
                ('branch_name', models.CharField(default='', max_length=20)),
                ('account_number', models.CharField(default='', max_length=20)),
                ('ifsc_code', models.CharField(default='', max_length=20)),
                ('aadhar_number', models.CharField(default='', max_length=20)),
                ('pancard_number', models.CharField(default='', max_length=20)),
                ('descripation', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='student')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
            ],
        ),
    ]
