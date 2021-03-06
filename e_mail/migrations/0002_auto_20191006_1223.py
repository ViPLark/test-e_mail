# Generated by Django 2.2.6 on 2019-10-06 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inbox',
            old_name='received_dt',
            new_name='add_dt',
        ),
        migrations.RenameField(
            model_name='sent',
            old_name='send_dt',
            new_name='add_dt',
        ),
        migrations.RemoveField(
            model_name='sent',
            name='to_user',
        ),
        migrations.AddField(
            model_name='inbox',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sent',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_email_set', to=settings.AUTH_USER_MODEL, verbose_name='from'),
        ),
        migrations.AlterField(
            model_name='email',
            name='to_users',
            field=models.ManyToManyField(related_name='inbox_email_set', to=settings.AUTH_USER_MODEL, verbose_name='to'),
        ),
    ]
