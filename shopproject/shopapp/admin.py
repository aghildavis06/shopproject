from django.contrib import admin

from shopapp.models import Category,Product

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,AdminCategory)

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product,AdminProduct)