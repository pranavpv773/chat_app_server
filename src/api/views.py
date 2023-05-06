from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import EmailOtpData
from django.core.mail import send_mail
from django.conf import settings
import pyotp

class EmailSenderView(APIView):
    def post(self,request):
        email = request.data.get("email")
        totp = pyotp.TOTP('base32secret3232',digits=4,interval=5)
        otp = totp.now()
        EmailOtpData.objects.create(otp = otp)
        subject = 'Verification code for ChatApp'
        message=f'Your otp Verification code  is {otp}'
        email_from = settings.EMAIL_HOST_USER
        send_mail(
        subject,
        message,
        email_from,
        [email]
        )
        return Response({"success":"otp send successfully"},status=status.HTTP_200_OK)
class EmailVeficationView(APIView):
    def post(self,request):
        otp = request.data.get('otp')
        try:
           check_otp = EmailOtpData.objects.get(otp = otp)
           check_otp.is_verified = True
           check_otp.save()
           return Response({"success":"otp verified"},status=status.HTTP_200_OK)
        except:
           return Response({"error":"otp is not correct"},status=status.HTTP_200_OK)
        