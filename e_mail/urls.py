from django.urls import path

from .views import EmailView, InboxListView, InboxDetailView, SentListView, SentDetailView

app_name = 'email'

urlpatterns = [
    path('create/', EmailView.as_view()),
    path('inbox/<int:pk>', InboxDetailView.as_view()),
    path('inbox/', InboxListView.as_view()),
    path('sent/<int:pk>', SentDetailView.as_view()),
    path('sent/', SentListView.as_view()),
]
