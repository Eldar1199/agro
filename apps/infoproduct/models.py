from django.db import models
from slugify import slugify
from PIL import Image


class InfoCategory(models.Model):
    name = models.CharField(max_length = 100, 
                             unique = True, 
                             verbose_name = 'Названиее категории')
    slug = models.SlugField(max_length = 30, 
                            primary_key = True, 
                            blank = True) 

    def __str__(self) -> str:
        return self.name


class Infoproduct(models.Model):
    categories = models.ForeignKey(InfoCategory, 
                                   on_delete = models.CASCADE, 
                                   related_name = 'infoproduct', 
                                   verbose_name = 'Категория')

    name = models.CharField(max_length = 20)
    title = models.TextField()
    desc = models.TextField()
    process = models.TextField()
    image1 = models.ImageField(upload_to='products_phoots/')
    image2 = models.ImageField(upload_to='products_phoots/')
    image3 = models.ImageField(upload_to='products_phoots/')

    MAX_IMAGE_SIZE = (200, 200)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize images if needed
        for field_name in ['image1', 'image2', 'image3']:
            image = getattr(self, field_name)
            if image:
                img = Image.open(image.path)
                if img.width > self.MAX_IMAGE_SIZE[0] or img.height > self.MAX_IMAGE_SIZE[1]:
                    img.thumbnail(self.MAX_IMAGE_SIZE)
                    img.save(image.path)