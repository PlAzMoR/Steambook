from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(verbose_name = "Заголовок",
        max_length = 90)
    text = models.TextField(verbose_name = "Текст",
        max_length = 2000)
    author = models.ForeignKey(User, verbose_name = "Автор",
        related_name = "post_author", on_delete = models.CASCADE)
    price = models.CharField(verbose_name = "Цена предложения",
        max_length = 20, default = "Цена не указана")
    pub_date = models.DateTimeField(verbose_name = "Дата публикации",
        auto_now_add = True)


    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def __str__(self):
        return self.title[:30]
