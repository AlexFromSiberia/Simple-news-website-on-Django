from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('add_an_article', views.add_an_article, name='add_an_article'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='DetailView'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='ArticleUpdate'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(), name='ArticleDelete'),
    path('by_rubric/<int:pk>/', views.by_rubric, name='by_rubric'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

