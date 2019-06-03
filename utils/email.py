import threading

from django.conf import settings
from django.core.mail import send_mail


def _send_email(subject, message, email, html_message):
    try_cnt = 0
    while try_cnt < 3:
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], html_message=html_message)
            try_cnt = 3
        except Exception as e:
            print(e)
            try_cnt += 1


def send_email(subject, message, email, html_message):
    thread = threading.Thread(target=_send_email, args=(subject, message, email, html_message))
    thread.start()
