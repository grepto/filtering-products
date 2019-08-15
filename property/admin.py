from django.contrib import admin

from .models import Flat, Claim


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building',)


class ClaimAdmin(admin.ModelAdmin):
    list_display = ('flat', 'user')
    raw_id_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
