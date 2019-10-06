from rest_framework.generics import CreateAPIView

from .serializers import EmailSerializer


class EmailView(CreateAPIView):
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        serializer.validated_data['from_user'] = self.request.user
        instance = serializer.save()
        instance.send()
