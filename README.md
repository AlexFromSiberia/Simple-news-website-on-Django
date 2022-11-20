
## Это проект новостного сайта на Django, в котором реализовано:
- просмотр новостей, отсортированных по рубрикам;
- пагинация (pagination);
- вывод сообщений об успешных операциях/ошибках (messages)
- авторизация пользователей с разделением функционала;
- добавление / удаление / редактирование статей зарегестрированными пользователями;
- вывод статей по рубрикам;
- вывод популярных статей;
- редактироватие статей с помощью CKeditor;
- защита от ботов Captcha;
- установлен DDT (Django Debug Toolbar) для поиска проблем и отладки;
- настроена упрощённая отправка email администратору сайта из предусмотренной формы на сайте;
- кастомизирован внешний вид панели администратора, настроено: поиск по темам, фильтрация по рубрикам и авторам новостей.
- реализован API (через DRF: http://http://alexfromsiberia.site/news/api/v1/NewsArticles/). Ограничения для API: Просмотр - все пользователи. Редактирование - только зарегестрированные пользователи. Троттлинг - 10000 в день лимит для зарегестрированных, 1000 для анонимных.
- Безопасность: установлен Dotenv, все пароли загружаются из переменных системного окружения.



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
