from django.contrib import admin
from .models import Food,Review
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title','description','url')
    search_fields = ['title','description','url']
    list_editable = ('description','url',)
admin.site.register(Food,FoodAdmin)
admin.site.register(Review)