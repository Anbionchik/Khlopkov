from django.db import models
# from django.contrib.auth.models import User


class ListItemModel(models.Model):
    """ Модель списка дел в списке дел """
    name = models.CharField(max_length=128, verbose_name='Наименование задачи')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    listmodel_id = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)  # Без импорта лучше
    is_done = models.BooleanField(default=False)
    expiration_date = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super().save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список задач'
        unique_together = ('listmodel_id', 'name', 'expiration_date')
