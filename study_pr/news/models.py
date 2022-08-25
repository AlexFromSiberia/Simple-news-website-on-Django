from django.db import models
from django.contrib.auth.models import User


class Rubric(models.Model):
    name = models.CharField(max_length=150,
                            help_text="Enter the article's rubric",
                            verbose_name="The article's rubric")

    def __str__(self):
        return self.name


class NewsArticles(models.Model):
    title = models.CharField('name', max_length=100)
    text = models.TextField('full_text')
    date = models.DateField('Date', auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="Select the author",
                               verbose_name="Author",
                               null=True, blank=True)

    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT,
                               help_text="Choose the rubric",
                               verbose_name="Rubric",
                               null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "News article"
        verbose_name_plural = "News articles"
