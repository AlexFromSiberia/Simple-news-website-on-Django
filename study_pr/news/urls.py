from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('add_an_article', views.add_an_article, name='add_an_article'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='DetailView'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='ArticleUpdate'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(), name='ArticleDelete'),
    path('by_rubric/<int:rubric_id>/', views.by_rubric, name='by_rubric'),

]