from django.db import models

class school(models.Model):
    title = models.CharField(max_length=60)
    instructorName = models.CharField(max_length=60)
    courseNum = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    #def __str__(self):
        #return self.instructorName

    #def __str__(self):
        #return self.courseNum + self.duration
