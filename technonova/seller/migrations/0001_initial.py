# Generated by Django 4.0 on 2022-01-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.FileField(default='product', upload_to='products')),
            ],
            options={
                'db_table': 'decorations',
            },
        ),
    ]