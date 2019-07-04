from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=64, default="")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Instance(models.Model):
    name = models.CharField(max_length=64, default="")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DataEntry(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class GraphSelector(models.Model):
    name = models.CharField(max_length=64, default="")
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT)

    color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return str(self.type) + ' ' + str(self.instance)


class Graph(models.Model):
    name = models.CharField(max_length=64, default="")
    title = models.CharField(max_length=64, default="")
    active = models.BooleanField(default=True)
    selector = models.ManyToManyField(GraphSelector)

    def __str__(self):
        return self.name
