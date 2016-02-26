from django.contrib import admin

from storage.models import (Container, ContainerSupertype, ContainerType,
                            Stock, Stockable, StockableType)


class StockableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
    )

    list_filter = (
        'type',
    )


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'stockable',
        'date_prepared',
        'prepared_by',
    )

    list_filter = (
        'prepared_by',
    )

    search_fields = (
        'stockable__type__name',
    )

    raw_id_fields = (
        'stockable',
    )


class ContainerTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'supertype',
        'slots_vertical',
        'slots_horizontal',
    )

    list_filter = (
        'supertype',
    )

    search_fields = (
        'name',
    )


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'parent',
        'vertical_position',
        'horizontal_position',
        'owner',
        'is_thawed',
    )

    list_filter = (
        'type__supertype',
        'owner',
        'is_thawed',
    )

    search_fields = (
        'name',
        'owner__username',
        'owner__first_name',
        'owner__last_name',
    )

    raw_id_fields = (
        'parent',
        'stock',
    )

    fieldsets = (
        (None,
            {'fields': (
                'name', 'type', 'parent', 'vertical_position',
                'horizontal_position', 'owner', 'notes',
            )}),
        ('Relevant for tubes/wells only',
            {'fields': (
                'stock', 'is_thawed', 'thawed_by', 'date_thawed',
                'thaw_results',
            )}),
    )


admin.site.register(Container, ContainerAdmin)
admin.site.register(ContainerSupertype)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Stockable, StockableAdmin)
admin.site.register(StockableType)
