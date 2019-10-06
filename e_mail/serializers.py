from django.contrib import messages
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User, Email, Inbox


class UserEmailSerializer(serializers.EmailField):
    def get_choices(self, value):
        return {u.email: u.email for u in User.objects.all()}

    def to_representation(self, value):
        return value.email


class EmailSerializer(serializers.ModelSerializer):
    FROM = UserEmailSerializer(read_only=True, source='from_user')
    TO = serializers.ManyRelatedField(UserEmailSerializer(), source='to_users')

    class Meta:
        model = Email
        fields = ('FROM', 'TO', 'title', 'text')

    def validate_TO(self, value):
        request = self.context['request']
        users = []
        for email in set(value):
            try:
                users.append(User.objects.get(email=email))
            except User.DoesNotExist:
                messages.error(request, f'Email address "{email}" does not exist')
        if users:
            emails_string = '", "'.join((u.email for u in users))
            message = f'Email sent to: "{emails_string}"'
            messages.success(request, message)
            return users

        raise ValidationError('Check the email addresses into the "TO" field')


class InboxSerializer(serializers.ModelSerializer):
    FROM = serializers.EmailField(source='email.from_user.email')
    title = serializers.CharField(source='email.title')
    text = serializers.CharField(source='email.text')

    class Meta:
        model = Inbox
        fields = ('FROM', 'title', 'text', 'is_new')
