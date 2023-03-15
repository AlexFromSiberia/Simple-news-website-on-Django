
## Это проект новостного сайта на Django, в котором реализовано:
- Celery + Redis использованы для выполнения задач отправки email администратору сайта (страница "Contacts");
- Dotenv: все пароли загружаются из переменных системного окружения.
- Captcha: защита от ботов;
- просмотр новостей, отсортированных по рубрикам, добавление / удаление / редактирование статей зарегистрированными пользователями;
- пагинация;
- авторизация пользователей с разделением функционала;
- вывод статей по рубрикам;
- вывод популярных статей;
- редактирование статей с помощью CKeditor;
- установлен DDT (Django Debug Toolbar) для поиска проблем и отладки;
- кастомизирован внешний вид панели администратора, настроено: поиск по темам, фильтрация по рубрикам и авторам новостей.
- Реализован API (через DRF: http://http://alexfromsiberia.site/news/api/v1/NewsArticles/). Ограничения для API: Просмотр - все пользователи. Редактирование - только зарегистрированные пользователи. Троттлинг - 10000 в день лимит для зарегистрированных, 1000 для анонимных.



---

## This is a Django 'news site' project that implements:
- viewing news sorted by headings;
- pagination;
- authorization of users and functionality separation;
- error/success messages at the top of the screen; 
- adding / deleting / updating articles by registered users;
- search of articles by headings;
- output of popular articles;
- editing articles with CKeditor;
- bot protection Captcha;
- installed DDT (Django Debug Toolbar) for troubleshooting and debugging;
- simplified sending email to the site administrator right from the site;
- customized admin panel, configured: appearance, search by topics, filtering by headings and authors.
- API implemented (via DRF: http://http://alexfromsiberia.site/news/api/v1/NewsArticles/). API restrictions: View - all users. Editing - only registered users. Throttling - 10000 per day limit for registered, 1000 for anonymous.
- Security: Dotenv is installed, all passwords are loaded from system environment variables.
