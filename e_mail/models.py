from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Email(models.Model):
    from_user = models.ForeignKey(User, verbose_name='from', on_delete=models.PROTECT, related_name='sent_email_set')
    to_users = models.ManyToManyField(User, verbose_name='to', related_name='inbox_email_set')
    title = models.CharField(max_length=500)
    text = models.TextField()

    # service
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def send(self):
        Sent.objects.create(user=self.from_user, email=self, is_new=False)
        inbox_letters = (
            Inbox(user=to_user, email=self) for to_user in self.to_users.all()
        )
        Inbox.objects.bulk_create(inbox_letters)


class Catalog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.DO_NOTHING)
    is_new = models.BooleanField(default=True)

    # service
    add_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.email.title


class Inbox(Catalog):
    class Meta:
        verbose_name_plural = 'Inbox emails'


class Sent(Catalog):
    class Meta:
        verbose_name_plural = 'Sent emails'
