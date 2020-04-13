from django.db import models

# Create your models here.
kategori = (
    ('1','Bursaspor'),
    ('2','Bursa')
)
class Post(models.Model):
    title = models.CharField(max_length = 120)
    categorie = models.CharField(choices =kategori,max_length =25)
    date = models.DateTimeField(auto_now=True,verbose_name='Tarih')
    home = models.CharField(choices = (('1','Anasayfada Goster'),('2','Anasayfada Gosterme')),max_length = 10,default ='1')
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now=True, verbose_name='Tarih')
    category = models.CharField(choices = kategori,max_length =25)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField()
    url = models.URLField(max_length = 200)