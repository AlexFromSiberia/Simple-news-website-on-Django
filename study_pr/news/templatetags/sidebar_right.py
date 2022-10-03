from django import template
from ..models import NewsArticles

register = template.Library()


@register.inclusion_tag('news/popular_articles_tpl.html')
def get_popular_articles(cnt=3):
    articles = NewsArticles.objects.order_by('-views')[:cnt]
    return {'articles': articles}

