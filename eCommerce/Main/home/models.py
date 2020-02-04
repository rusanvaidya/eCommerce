from django.db import models

# Create your models here.


class banner(models.Model):
    company = models.CharField(max_length=100, blank=False)
    img_banner = models.ImageField(upload_to='banner_images')

    def __str__(self):
        return self.company


class sub_banner(models.Model):
    brand = models.CharField(max_length=100, blank=False)
    img_sub_banner = models.ImageField(upload_to='sub_banners_images')

    def __str__(self):
        return self.brand


class products(models.Model):
    item = models.CharField(max_length=200, blank=False)
    old_price = models.IntegerField()
    price = models.IntegerField(blank=False)
    brand = models.CharField(max_length=100,blank=False)
    category = models.CharField(max_length=100,blank=False)
    detail = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500,blank=False)
    availability = models.CharField(max_length=100,blank=False)
    for_gender = models.CharField(max_length=100)
    img_product = models.ImageField(upload_to='product')

    def __str__(self):
        return self.item


class ads(models.Model):
    img_ads = models.ImageField(upload_to='ads')
    brand = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.brand

class order_product(models.Model):
    item_info = models.TextField(max_length=700, blank=False)
    pay_method = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    address = models.TextField(max_length=700)
    phone = models.IntegerField()

    def __str__(self):
        return self.item_info

class review_product(models.Model):
    product_id = models.IntegerField()
    sender = models.CharField(max_length=200)
    review_text = models.TextField(max_length=700)
    rating = models.IntegerField()

class contact_us(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    enquiry = models.TextField(max_length=700)


