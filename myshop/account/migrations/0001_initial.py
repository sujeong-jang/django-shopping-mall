# Generated by Django 3.0.8 on 2020-08-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
