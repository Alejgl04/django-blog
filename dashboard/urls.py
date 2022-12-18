
from django.urls import path
from .views import DashboardHomeView, NewsLetterDashboardHomeView, NewsLetterCreateView, NewsLetterDetailView, NewsLetterUpdateView, NewsLetterDeleteView


app_name="dashboard"

urlpatterns = [
  path('', DashboardHomeView.as_view(), name="home"),
  path('list/', NewsLetterDashboardHomeView.as_view(), name="list"),
  path('create/', NewsLetterCreateView.as_view(), name="create"),
  path('detail/<int:pk>', NewsLetterDetailView.as_view(), name="detail"),
  path('update/<int:pk>', NewsLetterUpdateView.as_view(), name="update"),
  path('delete/<int:pk>', NewsLetterDeleteView.as_view(), name="delete"),
]
