from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    # 마지막 30번째 메시지까지 로드
    def last_30_messages(self):
        return Message.objects.order_by('-timestamp').all()[:30]

    # 마지막 10번째 메시지까지 로드
    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]