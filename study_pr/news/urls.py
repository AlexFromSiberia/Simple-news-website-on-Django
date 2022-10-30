from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'NewsArticles', views.NewsArticlesViewSet)


urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('add_an_article', views.add_an_article, name='add_an_article'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='DetailView'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='ArticleUpdate'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(), name='ArticleDelete'),
    path('by_rubric/<int:pk>/', views.by_rubric, name='by_rubric'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # http://127.0.0.1:8000/news/api/v1/NewsArticles/  + int: pk of article if needed
    path('api/v1/', include(router.urls)),
    # auto авторизация session-based
    # http://127.0.0.1:8000/news/api-auth/login
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

