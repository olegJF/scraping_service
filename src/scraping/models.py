from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населенного пункта')
    slug = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'
        
    def __str__(self):
        return self.name
