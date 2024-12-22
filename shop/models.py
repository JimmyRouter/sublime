from django.db import models
from django.urls import reverse


class Categories(models.Model):
    cat_tag = models.CharField(max_length=31)
    cat_name = models.CharField(max_length=63)
    cat_description = models.CharField(max_length=1023)

    def __str__(self):
        return str(self.cat_tag)


class Units(models.Model):
    unit_tag = models.CharField(max_length=31)
    unit_name = models.CharField(max_length=63)
    unit_okei = models.CharField(max_length=10, default='000', null=True, blank=True)

    def __str__(self):
        return str(self.unit_tag)


class Product(models.Model):
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tag = models.CharField(max_length=31)
    name = models.CharField(max_length=63)
    description = models.TextField()
    unit = models.ForeignKey(Units, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products', blank=True, null=True)
    ico = models.ImageField(upload_to='products', blank=True, null=True, default='noico.png')

    def list_description(self, splitter: str='\n'):
        aslist = str(self.description).split(splitter)
        # print('models serv descr as list>>>>>', aslist)
        return aslist

    def __str__(self):
        return str(self.tag)

    def get_absolute_url(self):
        return reverse('this_service', kwargs={'service_tag': self.tag})


class Tickets(models.Model):
    client_email = models.EmailField()
    client_phone = models.IntegerField(blank=True, null=True)
    client_name = models.CharField(max_length=64, blank=True,null=True)
    ticket_subject = models.TextField(blank=True, null=True)