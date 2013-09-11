from django.contrib import admin
from storage.models import *

class StockableAdmin(admin.ModelAdmin):
	list_display = (
		'__unicode__',
		'type',
	)
	list_filter = ('type',)

class StockAdmin(admin.ModelAdmin):
	list_display = (
		'stockable',
		'concentration',
		'prepared_by',
		'date_prepared',
	)
	list_filter = ('prepared_by',)

class ContainerTypeAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'supertype',
		'slots_vertical',
		'slots_horizontal',
	)
	list_filter = ('supertype',)

class ContainerAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'type',
		'owner',
		'parent',
		'vertical_position',
		'horizontal_position',
		'stock',
	)
	list_filter = ('type', 'owner')

admin.site.register(StockableType)
admin.site.register(Stockable, StockableAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(ContainerSupertype)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(Container, ContainerAdmin)
