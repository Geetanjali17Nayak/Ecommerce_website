from django.conf import settings
from django.core.mail import send_mail



def send_account_activation_mail(email, email_token):
    subject= "Your account need to br verified"
    email_from = settings.EMAIL_HOST_USER
    message=f'hi!! Click on the given link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject, message, email_from, [email], fail_silently=False)