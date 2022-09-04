from django.shortcuts import render
from django.urls import reverse_lazy
from .models import NewsArticles, Rubric
from .forms import AddArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator


def news_index(request):
    # add a join for 'rubric'
    all_news = NewsArticles.objects.select_related('rubric').all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = { 'rubrics': rubrics, 'page_obj': page_obj}
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
    error = ''
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
        else:
            error = 'Something went wrong, please check all the data add fill form again.'
    form = AddArticleForm()
    context = {'form': form, 'error': error}
    return render(request, 'news/add_an_article.html', context)


class ArticleDetailView(DetailView):
    model = NewsArticles
    template_name = 'news/detailed_view.html'
    context_object_name = 'article'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    model = NewsArticles
    template_name = 'news/update_an_article.html'
    form_class = AddArticleForm
    success_url = reverse_lazy("news_index")
    permission_required = 'news.can_delete_news_article'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    model = NewsArticles
    success_url = '/news/'
    template_name = 'news/article_delete.html'
    permission_required = 'news.can_delete_news_article'



