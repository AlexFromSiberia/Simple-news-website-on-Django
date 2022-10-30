from rest_framework import serializers
from .models import NewsArticles


class NewsArticlesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NewsArticles
        # all fields = model's fields
        # ("title", "text", "author", "rubric")
        fields = '__all__'

