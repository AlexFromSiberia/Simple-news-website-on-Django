from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NewsArticlesSerializer
from .models import NewsArticles, Rubric
from .forms import AddArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
# для возможности подсчёта просмотров
from django.db.models import F


def news_index(request):
    # add a join for 'rubric'
    all_news = NewsArticles.objects.select_related('rubric').all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'rubrics': rubrics, 'page_obj': page_obj}
    return render(request, 'news/news_index.html', context)


def by_rubric(request, pk):
    # add a join for 'rubric'
    all_news = NewsArticles.objects.filter(rubric_id=pk).select_related('rubric')
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=pk)
    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'news/news_index.html', context)


def add_an_article(request):
    def make_slug(title):
        """Makes a slug from the articles title, that user provides
        """
        f = [":", "?", "#", "[", "]", "@", "!", "$", "&", "'", "(", ")", "*", "+", ",", ";", "=", " "]
        ans = ''
        for letter in title:
            if letter not in f:
                ans += letter.lower()
            else:
                if ans[-1] == '_':
                    pass
                else:
                    ans += '_'
        return ans

    error = ''
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.slug = make_slug(form.cleaned_data['title'])
            new_article.save()
            return HttpResponseRedirect(reverse_lazy('news_index'))
        else:
            error = 'Something went wrong, please check all the data add fill form again.'
    form = AddArticleForm()
    context = {'form': form, 'error': error}
    return render(request, 'news/add_an_article.html', context)


class ArticleDetailView(DetailView):
    model = NewsArticles
    template_name = 'news/detailed_view.html'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class ArticleUpdate(SuccessMessageMixin, UpdateView, PermissionRequiredMixin, ):
    model = NewsArticles
    template_name = 'news/update_an_article.html'
    form_class = AddArticleForm
    success_url = reverse_lazy("news_index")
    permission_required = 'news.can_delete_news_article'
    success_message = 'Article has been successfully updated!'


class ArticleDelete(SuccessMessageMixin, DeleteView, PermissionRequiredMixin):
    model = NewsArticles
    success_url = reverse_lazy("news_index")
    template_name = 'news/article_delete.html'
    permission_required = 'news.can_delete_news_article'
    success_message = 'Article has been successfully deleted!'


# Django Rest Framework
class NewsArticlesViewSet(viewsets.ModelViewSet):
    queryset = NewsArticles.objects.all()
    serializer_class = NewsArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



