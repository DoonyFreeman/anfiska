from django.contrib import admin

from .models import IceCream


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_available")
    list_filter = ("is_available",)
    search_fields = ("title",)
