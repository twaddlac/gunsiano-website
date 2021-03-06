from django.contrib import admin

from storage.models import (Container, ContainerType, ContainerSupertype,
                            Stock)


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
        'type',
        'name',
        'owner',
        'is_thawed',
    )

    list_filter = (
        'owner',
    )

    ordering = (
        'id',
    )

    search_fields = (
        'id',
        'name',
        'type__name',
    )

    raw_id_fields = (
        'parent',
        'stock',
    )

    fieldsets = (
        (None, {'fields': (
            'type',
            'name',
            'owner',
            'notes',
        )}),
        ('Position', {'fields': (
            'parent',
            'vertical_position',
            'horizontal_position',
        )}),
        ('Stock', {'fields': (
            'stock',
            'is_thawed',
            'thawed_by',
            'date_thawed',
            'thaw_results',
        )}),
    )


class ContainerInline(admin.TabularInline):
    model = Container
    extra = 1

    raw_id_fields = (
        'parent',
    )

    # Define field order so that thawing fields precede name & owner
    # (since thawing fields are more commonly used with StockAdmin)
    fields = (
        'type',
        'parent',
        'vertical_position',
        'horizontal_position',
        'is_thawed',
        'thawed_by',
        'date_thawed',
        'thaw_results',
        'name',
        'owner',
        'notes',
    )


class StockAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'stockable',
        'prepared_by',
        'date_prepared',
    )

    list_filter = (
        'prepared_by',
    )

    search_fields = (
        'stockable__id',
    )

    raw_id_fields = (
        'stockable',
    )

    fields = (
        'stockable',
        'prepared_by',
        'date_prepared',
        'concentration',
        'notes',
    )

    inlines = [ContainerInline]


admin.site.register(Container, ContainerAdmin)
admin.site.register(ContainerSupertype)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(Stock, StockAdmin)
