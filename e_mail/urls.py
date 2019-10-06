from django.urls import path

from .views import EmailView, InboxListView, SentListView

app_name = 'email'

urlpatterns = [
    path('create/', EmailView.as_view()),
    path('inbox/', InboxListView.as_view()),
    path('sent/', SentListView.as_view()),
]
