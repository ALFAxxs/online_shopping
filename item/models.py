from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid


# class MyUser(AbstractUser):   #AbstaractUser ishlatilishi uchun ni djanog settings da AUTH_USER_MODEL = 'Core.MyUser' belgilash kerak
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )  #django admin panelda ordering (sanashni 1,2,3,4,5) faqat nomi bilan korsatadi
        verbose_name_plural = "Categories" #django admin panelda main name shunday nomlarnadi

    def __str__(self):
        return self.name  #django admin panelda nomlari bilan korishga yoradam beradi


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

