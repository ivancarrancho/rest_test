from django.contrib import admin

from .models import SavedEmbeds


@admin.register(SavedEmbeds)
class SavedEmbedsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'type',
        'provider_url',
        'provider_name',
        'title',
        'description',
        'html',
        'width',
        'height',
        'thumbnail_url',
        'thumbnail_width',
        'thumbnail_height',
        'author_url',
        'author_name',
        'version'
    )
