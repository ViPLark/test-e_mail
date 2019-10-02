from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Email(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_email_set')
    to_users = models.ManyToManyField(User, related_name='inbox_email_set')
    title = models.CharField(max_length=500)
    text = models.TextField()

    # service
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Inbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.DO_NOTHING)

    # service
    received_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Inbox emails'

    def __str__(self):
        return self.email.title


class Sent(models.Model):
    email = models.ForeignKey(Email, on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(User, on_delete=models.PROTECT)

    # service
    send_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sent emails'

    def __str__(self):
        return self.email.title

    @property
    def is_sent(self):
        return self.send_dt is not None
