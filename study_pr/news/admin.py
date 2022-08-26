from django.contrib import admin
from .models import NewsArticles, Rubric


class NewsArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'photo', 'author', 'rubric')
    list_display_links = ('id', 'title', 'date', 'photo', 'author')
    search_fields = ('title', )
    list_filter = ('author', 'rubric')


admin.site.register(Rubric)
admin.site.register(NewsArticles, NewsArticlesAdmin)

