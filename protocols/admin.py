from django.contrib import admin
from slugify import slugify

from protocols.models import Protocol


class ProtocolAdmin(admin.ModelAdmin):
    list_display = (
        'title_markdown',
        'author',
        'pub_date',
    )

    fields = ('title_markdown', 'author', 'body_markdown')

    def save_model(self, request, obj, form, change):
        # Set author to whoever is logged in
        if not obj.author:
            obj.author = request.user

        # If no url already given for this protocol, create it from the title
        if not obj.title_url:
            obj.title_url = slugify(obj.title_markdown)

        obj.save()


admin.site.register(Protocol, ProtocolAdmin)
