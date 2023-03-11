from study_pr.celery import app
from django.core.mail import send_mail


@app.task
def send_spam_email(subject, content, sender, receiver):
    mail = send_mail(
        subject,
        content,
        sender,
        [receiver],
        fail_silently=False,
    )
    return mail


