# Generated by Django 3.0.2 on 2020-01-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='latest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='imgmenu')),
            ],
        ),
    ]