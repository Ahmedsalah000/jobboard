from django.db import models

# Create your models here.
Job_Type=(
    ('Full Time','Full Time '),
    ('Part Time','Part Time'),
    
    
)

class Job (models.Model):
    title = models.CharField(max_length=50)
    job_type= models.CharField(max_length=50,choices=Job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True, null=True)
    #image = models.ImageField(upload_to=image_upload)

    #slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name