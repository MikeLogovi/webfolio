from django.db import models
from developpers.models import Developper
from django.template.defaultfilters import slugify
class Category(models.Model):
    class Meta:
        verbose_name ='Categorie'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
class Website(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.FileField(blank=True,default="default.png")
    image_url = models.URLField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    developper = models.ForeignKey(Developper,default=None,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)
    # Add in category later
    # Add in author later
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Website, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    def snippet(self):
        return self.description[0:20]