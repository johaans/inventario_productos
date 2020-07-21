from django.db import models
from django.utils import timezone
from datetime import datetime
from random import randint
from django.conf import settings
from django.urls import reverse
from django.forms.models import model_to_dict
from .choices import seleccion_cat
from inventario.settings import MEDIA_URL, STATIC_URL
from inventario.basemodel.models import BaseModel
from crum import get_current_user

# Create your models here.
class Bodegagenericos(models.Model):
    """Model definition for Bodegagenericos."""

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=400, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.IntegerField(default=0)
    nombre = models.CharField('NOMBRE', max_length=450)
    categoria=models.CharField('Categoria',choices=seleccion_cat,max_length=18)
    descripcion=models.TextField('DESCRIPCION',max_length=2000,null=True,blank=True)
    stockinicial = models.IntegerField(default=0)
    entradas = models.IntegerField(default=0)
    salidas = models.IntegerField(default=0)
    por = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    #total=(int(str(stockinicial))+int(str(entradas)))-int(str(salidas))
    final = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    veces = models.IntegerField(default=0)    
    imagen=models.ImageField('IMAGEN', upload_to='BODEGASGENERICOS', null=True, blank=True)

    class Meta:
        """Meta definition for Bodegagenericos."""

        verbose_name = 'Bodega generico'
        verbose_name_plural = 'Bodega genericos'

    def __str__(self):
        """Unicode representation of Bodegagenericos."""
        return self.nombre


class Bodegariester(models.Model):
    """Model definition for Bodegariester."""

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=400, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.IntegerField(default=0)
    nombre = models.CharField('NOMBRE', max_length=450)
    categoria=models.CharField('Categoria',choices=seleccion_cat,max_length=18)
    descripcion=models.TextField('DESCRIPCION',max_length=2000,null=True,blank=True)
    stockinicial = models.IntegerField(default=0)
    entradas = models.IntegerField(default=0)
    salidas = models.IntegerField(default=0)
    por = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    final = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    veces = models.IntegerField(default=0)    
    imagen=models.ImageField('IMAGEN', upload_to='BODEGASRIESTER', null=True, blank=True)
    class Meta:
        """Meta definition for Bodegariester."""

        verbose_name = 'Bodega riester'
        verbose_name_plural = 'Bodega riester'

    def __str__(self):
        """Unicode representation of Bodegariester."""
        self.nombre


class Bodegaotrasmarcas(models.Model):
    """Model definition for Bodegaotrasmarcas."""

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=400, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.IntegerField(default=0)
    nombre = models.CharField('NOMBRE', max_length=450)
    categoria=models.CharField('Categoria',choices=seleccion_cat,max_length=18)
    descripcion=models.TextField('DESCRIPCION',max_length=2000,null=True,blank=True)
    stockinicial = models.IntegerField(default=0)
    entradas = models.IntegerField(default=0)
    salidas = models.IntegerField(default=0)
    por = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    final = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    veces = models.IntegerField(default=0)    
    imagen=models.ImageField('IMAGEN', upload_to='BODEGASOTRASMARCAS', null=True, blank=True)


    class Meta:
        """Meta definition for Bodegaotrasmarcas."""

        verbose_name = 'Bodega otras marcas'
        verbose_name_plural = 'Bodega otras marcas'

    def __str__(self):
        """Unicode representation of Bodegaotrasmarcas."""
        return self.nombre


class Bodegas(models.Model):
    """Model definition for Bodegas."""

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=400, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.IntegerField(default=0)
    nombre = models.CharField('NOMBRE', max_length=100)
    categoria=models.CharField('Categoria',choices=seleccion_cat,max_length=18)
    descripcion=models.TextField('DESCRIPCION',max_length=2000,null=True,blank=True)
    stockinicial = models.IntegerField(default=0)
    entradas = models.IntegerField(default=0)
    salidas = models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    por = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    final = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    veces = models.IntegerField(default=0)    


    class Meta:
        """Meta definition for Bodegas."""

        verbose_name = 'Bodegas'
        verbose_name_plural = 'Bodegas'

    def get_absolute_url(self):
        return reverse('lista_repuestos')

    def __str__(self):
        """Unicode representation of categoria."""
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Producto(BaseModel):
    codigo = models.IntegerField(default=0,unique=True)
    nombre = models.CharField('NOMBRE', max_length=100)
    categoria=models.CharField('Categoria',choices=seleccion_cat,max_length=18)
    descripcion=models.TextField('DESCRIPCION',max_length=2000,null=True,blank=True)
    stockinicial = models.IntegerField(default=0)
    entradas = models.IntegerField(default=0)
    salidas = models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Producto, self).save()


    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Salida(models.Model):
    """Model definition for Salidas."""
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL,default=settings.AUTH_USER_MODEL, max_length=400, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    total=models.IntegerField(default=0)



    class Meta:
        """Meta definition for Salida."""

        verbose_name = 'Salidas'
        verbose_name_plural = 'Salidas'
        ordering = ['id']

    def __str__(self):
        """Unicode representation of Salidas."""
        return self.responsable.get_username()

    def toJSON(self):
        item = model_to_dict(self)
        item['responsable'] =self.responsable.get_username()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detsalida_set.all()]
        return item



class DetSalida(models.Model):
    salida = models.ForeignKey(Salida, on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    def __str__(self):
        return self.prod.nombre

    def toJSON(self):
        item = model_to_dict(self, exclude=['salida'])
        item['prod'] = self.prod.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de Salida'
        verbose_name_plural = 'Detalle de Salidas'
        ordering = ['id']