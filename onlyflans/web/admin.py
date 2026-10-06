from django.contrib import admin
from . import models


@admin.register(models.Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ("name", "is_private", "precio")
    list_filter = ("is_private",)
    search_fields = ("name", "description", "slug", "tags__name")


admin.site.register(models.ContactForm)
admin.site.register(models.Tag)
