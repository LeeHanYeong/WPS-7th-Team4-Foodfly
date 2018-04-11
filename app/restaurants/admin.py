from django.contrib import admin

from .models import (
    RestaurantCategory,
    RestaurantOrderType,
    RestaurantTag,
    Restaurant,

    MenuCategory,
    Menu,
)


class RestaurantAdmin(admin.ModelAdmin):
    pass


admin.site.register(RestaurantCategory)
admin.site.register(RestaurantOrderType)
admin.site.register(RestaurantTag)
admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(MenuCategory)
admin.site.register(Menu)
