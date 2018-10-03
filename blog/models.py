from django.db import models

#create a blog model
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')


#add the blog app to the settings

#create a migration

#migrate

#add to the admin
