from django.utils import timezone

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=64, default='')
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=8, default='', blank=True)

    def __str__(self):
        return self.name


class Instance(models.Model):
    name = models.CharField(max_length=64, default='')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DataEntry(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT)
    value = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.timestamp) + ' Type: ' + str(self.type) + ' Instance: ' + str(self.instance) + ' : ' + str(round(self.value))


class GraphSelector(models.Model):
    name = models.CharField(max_length=64, default='')
    title = models.CharField(max_length=64, default='', blank=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT)
    order = models.IntegerField(default=0)

    color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return str(self.type) + ' ' + str(self.instance)


class Graph(models.Model):
    name = models.CharField(max_length=64, default='')
    title = models.CharField(max_length=64, default='', blank=True)
    dashboard = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    selector = models.ManyToManyField(GraphSelector)

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Display(models.Model):
    name = models.CharField(max_length=64, default='')
    title = models.CharField(max_length=64, default='', blank=True)
    dashboard = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    selector = models.ForeignKey(GraphSelector, on_delete=models.PROTECT)

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Settings(models.Model):
    title = models.CharField(max_length=64, default='')
