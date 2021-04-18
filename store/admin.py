from django.contrib import admin
from store.models import Category ,Product




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name' ,) }
    list_display = ['name' , 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name' ,) }
    list_display = ['category','name', 'slug', 'price','available' ,'created' ,'updated']
    list_filter = ['category','name' , 'price','available' ,'created' ,'updated']
    list_editable = ['name' , 'price','available' ]
