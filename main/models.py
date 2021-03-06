from django.db import models

# from django.contrib.auth.models import User


class ListModel(models.Model):
    """ Модель списка дел """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Без импорта лучше
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список дел'
        unique_together = ('name', 'user')

