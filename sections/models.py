from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
# Create your models here.
class Page(models.Model):
    h1 = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='img', default='Нет изображения')

    def __str__(self):
        return self.title
