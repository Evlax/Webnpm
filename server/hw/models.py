from django.db import models


class First(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Название компании', max_length=150)



class Second(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название биллборда', max_length=150)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    fk = models.ForeignKey('First', on_delete=models.CASCADE)

