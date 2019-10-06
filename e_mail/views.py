from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Inbox, Sent
from .serializers import EmailSerializer, InboxSerializer, SentSerializer


class InboxListView(ListAPIView):
    serializer_class = InboxSerializer

    def get_queryset(self):
        return Inbox.objects.filter(user=self.request.user)


class SentListView(ListAPIView):
    serializer_class = SentSerializer

    def get_queryset(self):
        return Sent.objects.filter(user=self.request.user)


class EmailView(CreateAPIView):
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        serializer.validated_data['from_user'] = self.request.user
        instance = serializer.save()
        instance.send()
