from django.contrib import admin

from .models import (
    RestaurantCategory,
    RestaurantOrderType,
    RestaurantTag,
    Restaurant,

    MenuCategory,
    Menu,
)


class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'min_order_price',
        'delivery_price',
        # 'avg_delivery_time',
    )


admin.site.register(RestaurantCategory, RestaurantCategoryAdmin)
admin.site.register(RestaurantOrderType)
admin.site.register(RestaurantTag)
admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(MenuCategory)
admin.site.register(Menu)
