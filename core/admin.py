from django.contrib import admin

from . import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["author", "article"]

    search_fields = ("author",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "views",
        "display_image_in_admin",
        "category",
        "author",
    ]
    list_display_links = ["pk", "title"]
    list_filter = ["category", "author", "created_at"]
    list_editable = ["category", "author"]
    readonly_fields = ["views"]


admin.site.register(models.Comment)
