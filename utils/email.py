import threading

from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, email):
    thread = threading.Thread(target=send_mail, args=(subject, message, email))
    thread.start()


def _send_email(subject, message, email):
    try_cnt = 0
    while try_cnt <= 3:
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            try_cnt = 3
        except Exception as e:
            print(e)
            try_cnt += 1
