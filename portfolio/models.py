from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) # Title discription or Text, Header
    description = models.CharField(max_length=250) # Body text, the text below header
    image = models.ImageField(upload_to='portfolio/images/') # we store our images in portfolio/images/ just like templates
    url = models.URLField(blank=True) # we put blank because we want some of our pages to be clickable and some not. Blank is optional

    def __str__(self):
        return self.title
