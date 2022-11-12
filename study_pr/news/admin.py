from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsArticles, Rubric
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsArticlesForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsArticles
        fields = '__all__'


class NewsArticlesAdmin(admin.ModelAdmin):
    form = NewsArticlesForm
    save_as = True
    list_display = ('id', 'title', 'slug', 'date', 'photo', 'thumbnail', 'author', 'rubric')
    list_display_links = ('id', 'title', 'date', 'photo', 'author')
    search_fields = ('title', )
    list_filter = ('author', 'rubric')
    fields = ('title', 'slug', 'rubric', 'photo', 'thumbnail', 'text', 'author',  'date')
    readonly_fields = ('id', 'date', 'thumbnail')
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}

    def thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')


admin.site.register(Rubric)
admin.site.register(NewsArticles, NewsArticlesAdmin)

