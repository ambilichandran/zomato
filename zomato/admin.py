from django.contrib import admin
from .models import Hotel,Food,Fooditem,Detail
class DetailsAdmin(admin.ModelAdmin):
    list_display=['name','address','phone','email']
admin.site.register(Hotel)
admin.site.register(Food)
admin.site.register(Fooditem)
admin.site.register(Detail,DetailsAdmin)