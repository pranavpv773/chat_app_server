from django.urls import path
from .import views

urlpatterns = [
    path('send-email/',views.EmailSenderView.as_view() ),
    path('verify-otp/',views.EmailVeficationView.as_view() ),

]