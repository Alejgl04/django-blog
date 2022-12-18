from django.contrib import admin
from .models import NewsLetterUser, NewsLetter
# Register your models here.

admin.site.register( NewsLetterUser )
admin.site.register( NewsLetter )