from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class Categories(models.Model):
    name=models.CharField('Başlıq',max_length=200,unique=True)
    date=models.DateTimeField('Tarix',default=timezone.now)
    navbar=models.BooleanField('Kəllə',default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", default='time_person')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
class Articles(models.Model):
    name=models.CharField('Başlıq',max_length=200,unique=True)
    category=models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Bölmə',default='')
    autor=models.CharField('Müəllif',max_length=200,null=True,blank=True)
    img=models.URLField('Foto')
    img2=models.URLField('Foto iç şəkil',default='',null=True,blank=True)
    img3=models.URLField('Events üçün şəkil',default='',null=True,blank=True)
    video=models.CharField('Video',max_length=1000,null=True,blank=True,default='')
    txt=RichTextField('Məzmun', default='',null=True,blank=True)
    txt_desc=models.TextField('Qısa məzmun',default='', null=True,blank=True)
    slide=models.BooleanField('Orta Karusel',default=False)
    slide2=models.BooleanField('Cover Karusel',default=False)
    slide3=models.BooleanField("EDITOR'S PICKS",default=False)
    date=models.DateTimeField('Tarix',default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", default='time_person')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'