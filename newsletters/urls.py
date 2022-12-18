from django.urls import path
from .views import newsLetterSigNup, newsLetterUnSuscribe

app_name = "news"

urlpatterns = [
  path('signup/', newsLetterSigNup, name="optin"),
  path('unsuscribe/', newsLetterUnSuscribe, name="unsuscribe"),
]