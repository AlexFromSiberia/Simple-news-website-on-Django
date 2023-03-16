from django.test import TestCase
from news.models import NewsArticles
from django.urls import reverse


# launch all tests with `python manage.py test`
# тестируем модель
class NewsArticlesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        NewsArticles.objects.create(title='article name', text='some text here')

    def test_title(self):
        title = NewsArticles.objects.get(id=1)
        field_label = NewsArticles._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Title')

    def test_text_label(self):
        title = NewsArticles.objects.get(id=1)
        field_label = NewsArticles._meta.get_field('text').verbose_name
        self.assertEquals(field_label, "Full_text")

    def test_date_label(self):
        title = NewsArticles.objects.get(id=1)
        field_label = NewsArticles._meta.get_field('date').verbose_name
        self.assertEquals(field_label, "Date")

    def test_title_max_length(self):
        title = NewsArticles.objects.get(id=1)
        max_length = NewsArticles._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)


# тестируем views
class NewsListViewTest(TestCase):

    def test_mainpage_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_main_page_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news_index'))
        self.assertEqual(resp.status_code, 200)

    def test_news_view_url_exists_at_desired_location(self):
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 200)

    def test_news_page_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news_index'))
        self.assertEqual(resp.status_code, 200)

    def test_about_view_url_exists_at_desired_location(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)

    def test_about_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_add_an_article_view_url_exists_at_desired_location(self):
        resp = self.client.get('/news/add_an_article/')
        self.assertEqual(resp.status_code, 200)

    def test_add_an_article_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('add_an_article'))
        self.assertEqual(resp.status_code, 200)

    def test_contacts_url_exists_at_desired_location(self):
        resp = self.client.get('/contacts/')
        self.assertEqual(resp.status_code, 200)

    def test_contacts_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('contacts'))
        self.assertEqual(resp.status_code, 200)

    def test_accounts_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)

    def test_register_view_url_exists_at_desired_location(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)

    def test_register_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)

    def test_pagination_is_three(self):
        resp = self.client.get(reverse('news_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('page_obj' in resp.context)
        self.assertEqual(str(resp.context['page_obj']), '<Page 1 of 1>')

    def test_lists_all_authors(self):
        # Get second page
        resp = self.client.get(reverse('news_index') + '?page=2')
        self.assertEqual(resp.status_code, 200)


