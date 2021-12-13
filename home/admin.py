from django.contrib import admin

# Register your models here.

from . models import banner, sub_banner, products, ads, order_product, review_product, contact_us

class order_p(admin.ModelAdmin):
    list_display = ("full_name","address")
    readonly_fields = ["item_info","pay_method","sender","full_name","address","phone"]
    def has_add_permission(self,request):
        return False

class preview(admin.ModelAdmin):
    list_display = ("product_id",)
    readonly_fields = ["product_id","sender","review_text","rating"]
    def has_add_permission(self,request):
        return False

class contactq(admin.ModelAdmin):
    list_display = ("email",)
    readonly_fields = ["full_name","email","enquiry"]
    def has_add_permission(self,request):
        return False

admin.site.register(banner)
admin.site.register(sub_banner)
admin.site.register(products)
admin.site.register(ads)
admin.site.register(order_product,order_p)
admin.site.register(review_product,preview)
admin.site.register(contact_us,contactq)

