from django.urls import path

from .views import EmailView

app_name = 'email'

urlpatterns = [
    path('create/', EmailView.as_view()),
]
