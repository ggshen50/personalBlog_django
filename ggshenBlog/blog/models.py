from django.db import models


# ���±�
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=True)
    title_zh = models.CharField(max_length=50, blank=False, null=True)
    body = models.CharField(max_length=10000, blank=True, null=True)
    author = models.CharField(max_length=20, blank=False, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    read = models.IntegerField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    updateTime = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# ΢��¼��
class MiniRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.CharField(max_length=100, blank=False, null=True)
    recordTime = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.body


# ��Ƭ��
class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# ��Ƶ��
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
