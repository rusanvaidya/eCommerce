from urllib.parse import urlencode
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from rest_framework import viewsets

from . models import banner, sub_banner, products, ads, order_product, review_product, contact_us
from .serializers import UserSerializer


def home(request):
    banner_photo = banner.objects.all()
    sub_banner_photo = sub_banner.objects.all()
    prod_info = products.objects.all()
    ads_info = ads.objects.all()
    dict1 = {
        "banner_photo": banner_photo,
        "sub_banner_photo": sub_banner_photo,
        "p_info": prod_info,
        "ads_now": ads_info,
    }
    return render(request, 'index.html', dict1)


def product(request):
    if request.method == 'GET':
        p_id = request.GET.get('p_id')
        p_bd = request.GET.get('brand')
        review_get = review_product.objects.filter(product_id=p_id)
        prod_select = products.objects.filter(id=p_id, brand=p_bd)
        prod_info = products.objects.filter(~Q(id=p_id), brand=p_bd)
        prod_brand = products.objects.order_by('brand')
        prod_cat_w = products.objects.order_by('category').filter(for_gender='Women')
        prod_cat_m = products.objects.order_by('category').filter(for_gender='Men')
        prod_cat_k = products.objects.order_by('category').filter(for_gender='Kid')
        dict2 = {
            "p_select": prod_select,
            "p_info": prod_info,
            "p_brand": prod_brand,
            "p_cat_w": prod_cat_w,
            "p_cat_m": prod_cat_m,
            "p_cat_k": prod_cat_k,
            "review_get": review_get,
        }
        return render(request, 'product.html', dict2)
    if request.method == 'POST':
        product_id = request.POST.get('p_id')
        brand = request.GET.get('brand')
        sender = request.POST.get('sender')
        review_text = request.POST.get('review_text')
        rating_radio = request.POST.get('rating')
        new_review = review_product(product_id=product_id ,sender=sender,review_text=review_text,rating=rating_radio)
        new_review.save()
        base_url = reverse('product1')
        query_id =  urlencode({'p_id': product_id})
        query_brand =  urlencode({'brand': brand})
        url = '{}?{}'.format(base_url, query_id)
        url2 = '{}&{}'.format(url, query_brand)
        return redirect(url2) 

def category(request):
    prod = products.objects.all()

    if request.method == 'GET':
        search_item = request.GET.get('search')
        pfor = request.GET.get('gfor')
        type_s = request.GET.get('type')
        brand = request.GET.get('brand')
        view_for = products.objects.filter(for_gender=pfor)
        p_f_t = products.objects.filter(for_gender=pfor, category=type_s)
        brand_p = products.objects.filter(brand=brand)
        prod_brand = products.objects.order_by('brand')
        prod_cat_w = products.objects.order_by('category').filter(for_gender='Women')
        prod_cat_m = products.objects.order_by('category').filter(for_gender='Men')
        prod_cat_k = products.objects.order_by('category').filter(for_gender='Kid')
        search_p = products.objects.filter(for_gender=search_item)
        search_b = products.objects.filter(brand=search_item)
        search_for = products.objects.filter(category=search_item)
        search_i = products.objects.filter(item=search_item)
        
        dict3 = {
            "viewfor": view_for,
            "search_element": search_item,
            "prod": prod,
            "pfor": pfor,
            "type_s": type_s,
            "p_f_t": p_f_t,
            "brand": brand,
            "branded": brand_p,
            "p_cat_m": prod_cat_m,
            "p_brand": prod_brand,
            "p_cat_w": prod_cat_w,
            "p_cat_m": prod_cat_m,
            "p_cat_k": prod_cat_k,            
            "searchf": search_p,
            "searchb": search_b,
            "search_for":search_for,
            "search_i":search_i,
        }
        return render(request, 'category.html', dict3)

def aboutus(request):
    return render(request, 'about-us.html')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        enquiry = request.POST.get('enquiry')
        enquire = contact_us(full_name=full_name,email=email,enquiry=enquiry)
        enquire.save()
        return render(request,'contact.html')

    prod_brand = products.objects.order_by('brand')
    prod_cat_w = products.objects.order_by('category').filter(for_gender='Women')
    prod_cat_m = products.objects.order_by('category').filter(for_gender='Men')
    prod_cat_k = products.objects.order_by('category').filter(for_gender='Kid')
    dict0 = {
        "p_brand": prod_brand,
        "p_cat_w": prod_cat_w,
        "p_cat_m": prod_cat_m,
        "p_cat_k": prod_cat_k,
    }
    return render(request, 'contact.html', dict0)
    
def cart(request):
    return render(request,'cart.html')


def checkout(request):
    if request.method == 'POST':
        product_info = request.POST.get('itemJSON')
        pay_method = request.POST.get('pay_method')
        full_name = request.POST.get('full_name')
        sender = request.POST.get('sender')
        address = request.POST.get('address')
        phone = request.POST.get('tele')
        new_order = order_product(item_info=product_info, pay_method=pay_method, full_name=full_name,sender= sender,address=address, phone=phone)
        new_order.save()
        return redirect('/')
    return render(request,'checkout.html')

# def review(request):
    # if request.method == 'POST':

# def contact_form(request):


# API part
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer