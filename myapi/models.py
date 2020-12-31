from django.db import models

# Create your models here.
class Questions(models.Model):
    description= models.CharField(max_length=60)
    tags=models.CharField(max_length=60)
    title=models.CharField(max_length=30)
    creation_time=models.DateTimeField()
    user_id=models.IntegerField()
    count_view=models.IntegerField()

    def __str__(self):
        return self.title

class Answers(models.Model):
    aid=models.AutoField(primary_key=True)
    qid=models.IntegerField()
    desc=models.CharField(max_length=200)
    creation_time = models.DateTimeField()
    user_id = models.IntegerField()

