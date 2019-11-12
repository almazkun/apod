from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image_tub = models.CharField(max_length=300)
    image_full = models.CharField(max_length=300)
    date = models.DateField()
    explanation = models.TextField()


    def __str__(init):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.date)])
