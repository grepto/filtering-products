from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline, ]


class ClaimAdmin(admin.ModelAdmin):
    list_display = ('flat', 'user')
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
