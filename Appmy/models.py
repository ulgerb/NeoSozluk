from django.db import models

# Create your models here.


class Contentt(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Yazı"))
    yazar = models.CharField(("Yazar"), max_length=50)
    new_date = models.DateTimeField(("Yayınlanma Zamanı"), auto_now_add=True)


class Comments(models.Model):
    post = models.ForeignKey("Appmy.Contentt", verbose_name=("Post"), on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(("Ad"), max_length=50) 
    text = models.TextField(("Yorum"))
    com_date = models.DateTimeField(("Yorum Saati"), auto_now_add=True)

    class Meta:
        ordering = ['-com_date',]
