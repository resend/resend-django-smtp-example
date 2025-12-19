from django.http import JsonResponse
from django.core.mail import send_mail


def index(request):
    send_mail(
        subject="Hello from Resend",
        message="it works!",
        from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
        recipient_list=["delivered@resend.dev"],
    )
    return JsonResponse({"status": "ok"})