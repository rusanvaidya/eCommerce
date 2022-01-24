# Generated by Django 4.0 on 2022-01-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20200203_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='enquiry',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='full_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='address',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='item_info',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='pay_method',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='sender',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review_product',
            name='product_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review_product',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review_product',
            name='review_text',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='review_product',
            name='sender',
            field=models.CharField(max_length=200),
        ),
    ]
