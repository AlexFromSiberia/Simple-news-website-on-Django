
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
- реализована возможность просматривать и добавлять новостные статьи с помощью API (через DRF: для зарегистрированного пользователя: http://http://alexfromsiberia.site/news/api/v1/NewsArticles/)


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
- implemented ability to receive and add news articles using API (through Django Rest Framework: for registered user: http://http://alexfromsiberia.site/news/api/v1/NewsArticles/)
