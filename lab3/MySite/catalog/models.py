from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=150)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', blank=True)
    in_stock = models.BooleanField('В наличии', default=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    quantity = models.IntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at', '-pk']

    def __str__(self):
        return self.name
