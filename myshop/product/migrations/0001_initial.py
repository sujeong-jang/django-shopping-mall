# Generated by Django 3.0.8 on 2020-08-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('O', 'Outer'), ('T', 'Top'), ('S', 'Skirt'), ('P', 'Pants')], max_length=2)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='products')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]