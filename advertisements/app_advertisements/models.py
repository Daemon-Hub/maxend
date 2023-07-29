from django.db import models

class Advertisement(models.Model):
    class Meta:
        db_table = "advertisements"

    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Тогр", help_text="Уместен тогр или нет")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title}, price={self.price})"

