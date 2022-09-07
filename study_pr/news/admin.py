from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsArticles, Rubric


class NewsArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'photo', 'thumbnail', 'author', 'rubric')
    list_display_links = ('id', 'title', 'date', 'photo', 'author')
    search_fields = ('title', )
    list_filter = ('author', 'rubric')
    fields = ('title', 'rubric', 'photo', 'thumbnail', 'text', 'author',  'date')
    readonly_fields = ('id', 'date', 'thumbnail')

    def thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')


admin.site.register(Rubric)
admin.site.register(NewsArticles, NewsArticlesAdmin)

