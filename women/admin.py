from django.contrib import admin, messages

from women.models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщин"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ("title", "slug", "content", "category", "husband", "tags")
    list_display = ("id",
                    "title",
                    "category",
                    "time_created",
                    "is_published",
                    "brief_info")
    readonly_fields = ["slug"]
    list_filter = (MarriedFilter, "category", "is_published")
    search_fields = ("title", "category__title")
    filter_horizontal = ["tags"]
    ordering = ("-time_created",)
    # prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_per_page = 5
    actions = ['set_published', 'set_draft']

    @admin.display(description="Кроткое описание", ordering="content")
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов"

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
