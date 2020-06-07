from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def sendmail(request):

    name = request.POST['name']
    subject = request.POST['subject']
    from_email = request.POST['email']
    message = request.POST['message']

    send_mail(subject, message, from_email, [
              'admin@example.com'], fail_silently=False)

    return redirect('site')


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
