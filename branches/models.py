from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)
    # comment = models.TextField()

    def __str__(self):
        return self.name


class Periphery(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    

class Reception(models.Model):
    ip = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    printer = models.ManyToManyField(Periphery, related_name='receptions_printed')
    scaner = models.ManyToManyField(Periphery, related_name='receptions_scanned')
    scan_folder = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)

class QA(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

