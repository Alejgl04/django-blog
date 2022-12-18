from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings 

from django.template.loader import render_to_string
from django.views.generic import View

from newsletters.models import NewsLetterUser
from newsletters.forms import NewsLetterUserSignUpForm

class HomeView( View ):
  
  def get( self, request, *args, **kwargs):
    context = {}
    return render( request, 'index.html', context )
  
  def post( self, request, *args, **kwargs):
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
    return render( request, 'index.html', context )

class About( View ):
  
  def get( self, request, *args, **kwargs):
    context = {}
    return render( request, 'about.html', context )

class Contact( View ):
  
  def get( self, request, *args, **kwargs):
    context = {}
    return render( request, 'contact.html', context )
  
  
  def post( self, request, *args, **kwargs):
    
    messageName  = request.POST['full_name']
    messageEmail = request.POST['email']
    messagePhone = request.POST['phone']
    message      = request.POST['message']
    
    send_mail(
      messageName,
      message,
      messageEmail,
      ['aguerrerodev.web@gmail.com'],
    )
    messages.success(request, 'Message send successfully')
    
    context = {}
    return render( request, 'contact.html', context )