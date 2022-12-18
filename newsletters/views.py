from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

from django.conf import settings 
from django.shortcuts import render

from .models import NewsLetterUser
from .forms import NewsLetterUserSignUpForm
from django.template.loader import render_to_string


# Create your views here.

def newsLetterSigNup( request ):
  form = NewsLetterUserSignUpForm( request.POST or None )
  if form.is_valid():
    instance = form.save( commit= False )
    if NewsLetterUser.objects.filter( email = instance.email ).exists():
      messages.warning( request, 'Email already exist ')
    
    else:
      instance.save()
      messages.success( request, 'We sent an email to your email addrees, open to continued...')
      subject = 'Computer Books'
      fromEmail = settings.EMAIL_HOST_USER
      toEmail=[ instance.email ]
      
      htmlTemplate = 'newsletter/email_templates/welcome.html'
      htmlMessage = render_to_string(htmlTemplate)
      message = EmailMessage( subject, htmlMessage, fromEmail, toEmail )
      message.content_subtype = 'html'
      message.send()
  
  context = { 'form':form }
  return render( request, 'start-here.html', context )


def newsLetterUnSuscribe( request ):
  form = NewsLetterUserSignUpForm( request.POST or None )
  if form.is_valid():
    instance = form.save( commit= False )
    if NewsLetterUser.objects.filter( email = instance.email ).exists():
      NewsLetterUser.objects.filter( email = instance.email ).delete()
      messages.success( request, 'Email removed')
    else:
      print('Email not found')
      messages.warning( request, 'Email not found')

  context = {
    "form": form
  }
  return render( request, 'un_suscribe.html', context )
