# Generated by Django 4.0 on 2022-01-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_fullname', models.CharField(max_length=200)),
                ('customer_phonenumber', models.CharField(max_length=10)),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_username', models.CharField(max_length=100)),
                ('cutsomer_password', models.CharField(max_length=100)),
            ],
        ),
    ]
