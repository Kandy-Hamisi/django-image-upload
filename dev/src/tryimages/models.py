from django.db import models
# For media files to work I installed Pillow in my environment
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images') #upload_to specifies the location where images will be stored i.e MEDIA_ROOT/image

    ''' Even the below step works'''
    # image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
    