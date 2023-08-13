from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()
class Advertisement(models.Model):
    class Meta:
        db_table = "advertisements"

    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Тогр", help_text="Уместен тогр или нет")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            from django.utils.html import format_html
            return format_html(
                '''
                    <span style="color: green; font-weight: bold;">
                        Сегодня в {}
                    </span>
                ''',
                created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '''
                <span style="color: green; font-weight: bold;">
                    Сегодня в {}
                </span>
                ''',
                updated_time
            )
        return self.update_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Изображение')
    def mini_image(self):
        if self.image:
            return format_html(
                """
                    <img src='{}' width='60px'>
                """,
                self.image.url
            )
        return format_html(
            """
                <img src='/static/img/aidv.png' width='60px'>
            """
        )