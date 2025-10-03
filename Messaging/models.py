from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Conversation(models.Model):
     participants = models.ManyToManyField(
        User,
        related_name='Conversations',
        verbose_name='شرکت‌کنندگان'
    )
     last_message_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='آخرین زمان فعالیت'
    )
     class Meta:
        verbose_name = 'مکالمه'
        verbose_name_plural = 'مکالمات'
        ordering = ['-last_message_at']

     def __str__(self):
        return f"Conversation ({self.participants.count()} participants)"

class Message(models.Model):

     Conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='مکالمه'
     )

     sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='فرستنده'
     )

     content = models.TextField(
        verbose_name='متن پیام'
     )

     timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ارسال'
     )

     is_read = models.BooleanField(
        default=False,
        verbose_name='خوانده شده'
     )

     class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام‌ها'
        ordering = ['timestamp']

     def __str__(self):
        return f"Message from {self.sender} in {self.Conversation.id}: {self.content[:30]}..."
     
     
