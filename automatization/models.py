# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class FIO(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}, {}, {}'.format(self.name, self.surname, self.email)


class Files(models.Model):
    name = models.CharField(default=u'Name', max_length=50)
    which_user = models.ForeignKey(User)
    upload = models.FileField(upload_to='')

    def __unicode__(self):
        return '{}'.format(self.name)


class Template(models.Model):
    which_file = models.ForeignKey(Files)
    pages = models.CharField(max_length=2)

class Page1(models.Model):
    which_page1 = models.ForeignKey(Files)
    coorx1 = models.CharField(max_length=4)
    coory1 = models.CharField(max_length=4)
    text1 = models.CharField(max_length=100)
    coorx2 = models.CharField(max_length=4)
    coory2 = models.CharField(max_length=4)
    text2 = models.CharField(max_length=100)
    coorx3 = models.CharField(max_length=4)
    coory3 = models.CharField(max_length=4)
    text3 = models.CharField(max_length=100)
    coorx4 = models.CharField(max_length=4)
    coory4 = models.CharField(max_length=4)
    text4 = models.CharField(max_length=100)
    coorx5 = models.CharField(max_length=4)
    coory5 = models.CharField(max_length=4)
    text5 = models.CharField(max_length=100)
    coorx6 = models.CharField(max_length=4)
    coory6 = models.CharField(max_length=4)
    text6 = models.CharField(max_length=100)
    coorx7 = models.CharField(max_length=4)
    coory7 = models.CharField(max_length=4)
    text7 = models.CharField(max_length=100)
    coorx8 = models.CharField(max_length=4)
    coory8 = models.CharField(max_length=4)
    text8 = models.CharField(max_length=100)
    coorx9 = models.CharField(max_length=4)
    coory9 = models.CharField(max_length=4)
    text9 = models.CharField(max_length=100)
    coorx10 = models.CharField(max_length=4)
    coory10 = models.CharField(max_length=4)
    text10 = models.CharField(max_length=100)

