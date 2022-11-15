from django.db import models
from django.contrib.auth.models import User


class Rubric(models.Model):
    name = models.CharField(max_length=150,
                            help_text="Enter the article's rubric",
                            verbose_name="The article's rubric")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрику"
        verbose_name_plural = "Рубрики"


class NewsArticles(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    text = models.TextField(verbose_name='Full_text')
    date = models.DateField(verbose_name='Date', auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="Select the author",
                               verbose_name="Author",
                               null=True, blank=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT,
                               help_text="Choose the rubric",
                               verbose_name="Rubric",
                               null=True,
                               related_name='Articles')
    views = models.IntegerField(default=0, verbose_name='Views')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новостную статью"
        verbose_name_plural = "Новостные статьи"
