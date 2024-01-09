from django.contrib import admin

from women.models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "title",
                    "category",
                    "time_created",
                    "is_published",)
    list_filter = ("category", "tags")
    search_fields = ("title", )
    ordering = ("-time_created",)
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
