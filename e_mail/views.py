from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from .models import Inbox, Sent
from .serializers import EmailSerializer, InboxSerializer, SentSerializer


class DetailAPIView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        if 'new' in request.GET:
            instance = self.get_object()
            instance.is_new = request.GET['new']
            instance.save()
        return super().get(request, *args, **kwargs)


class InboxListView(ListAPIView):
    serializer_class = InboxSerializer

    def get_queryset(self):
        return Inbox.objects.filter(user=self.request.user)


class InboxDetailView(DetailAPIView, DestroyAPIView):
    serializer_class = InboxSerializer

    def get_queryset(self):
        return Inbox.objects.filter(user=self.request.user)


class SentListView(ListAPIView):
    serializer_class = SentSerializer

    def get_queryset(self):
        return Sent.objects.filter(user=self.request.user)


class SentDetailView(DetailAPIView, DestroyAPIView):
    serializer_class = SentSerializer

    def get_queryset(self):
        return Sent.objects.filter(user=self.request.user)


class EmailView(CreateAPIView):
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        serializer.validated_data['from_user'] = self.request.user
        instance = serializer.save()
        instance.send()
