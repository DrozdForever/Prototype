from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    CHOICE = (('male', 'Мужской'), ('female', 'Женский'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        'Фото пользователя',
        default='default.png',
        upload_to='user_images'
    )
    gender = models.CharField(
        'Пол пользователя',
        choices=CHOICE,
        max_length=16,
        null=True, blank=True
    )
    check = models.BooleanField('Согласие на рассылку', default=False)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)

        if image.height > 64 or image.width > 64:
            resize = (64, 64)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
