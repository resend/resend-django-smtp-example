import os
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection

def index(request):

    subject = "Hello from Django SMTP"
    recipient_list = ["delivered@resend.dev"]
    from_email = "onboarding@resend.dev"
    message = "<strong>it works!</strong>"

    with get_connection(
        host='smtp.resend.com',
        port=587,
        username='resend',
        password=os.environ["RESEND_API_KEY"],
        use_tls=True,
        ) as connection:
            r = EmailMessage(
                  subject=subject,
                  body=message,
                  to=recipient_list,
                  from_email=from_email,
                  connection=connection).send()
    return JsonResponse({"status": "ok"})
