# django_blog
This Project consist of two separate apps. Each app uses admin page and models.py. We use our built in Database (SQLite) to store our blogs. The idea to use multiple apps within one project as to avoid confusions and text cognations. Each app can represent blogs, profiles, accounts, photos and so on. Multiple apps help to organize your project. 

"	Go to your Bash Operator/ Terminal, cd Desktop, django-admin createproject project-name.
"	Run your server django manage.py runserver.
"	Create new apps, django-admin startapp app-names. 
"	Open your code editor(Atom)í go to settingsí Apps_Installedí add new apps. 

Create Models. 
"	Models are Data-Base, consist of Classes and Objects. Django makes is easy to use classes in order to create objects with attributes, just like we use classes in regular Python programming. We use Class and provide attributes in order to create instances. 

"	When we create Models with Django, we create objects, all objects are accessible for developers to use or edit at Back-End of our project (Admin-page). 

"	Now go to your first app and open Models.py í here we will create our Classí since this is Blog project we need to create attributes which will closely describe each Blog, you can customize your blog by reffering to Django Documentation:

      class Blog(models.Model):
               title=models.CharField(max_length = 100)í create title for our blog.
               description= models.CharField(max_length =250) í body or paragraph for our blog.
               image = models.ImageField(upload_to='portfolio/images/') í upload pictures.
               url = models.URLField(blank=True) íwe want some our pages to be clickable
               
               def __str__(self):
                      return slef.title í so we can see title names when we go to admin page. 

"	If we want to save our model we need to perform few steps í go to Terminal í python manage.py makemigrations (this command will start our transfer from Models.py to db.sqlite3) í python manage.py migrate (this command will move all savings to db.sqlite3)í python manage.py runserver. 
"	Go to admin.py í from .models import Blog í admin.site.register(Blog)

"	Now to write your first Blog you can go to your admin page ígo to Terminal í python manage.py createsuperuserícreate login, email, passwordílocalhost:8000/adminí access with your name and passwordí Once you there, create your first blog. 

Uploading Picture 

"	In order to upload picture to your project, you need to install pillow library, go to your terminal and do pip install pillow. 

"	Now to add pictureígo settings í MEDIA_ROOT = ( BASE_DIR / 'media') MEDIA_URL = '/media/' (this saves all media files). Once your create this file í go to Admin page and upload picture í go to your code editor again í look at your project you should see new file name media í this is where all your pictures should be saved in í go to urls.py  from django.conf.urls.static import static, from django.conf import settings, urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT). 

Now since we have two apps in one project, you can avoid all url hassle  by just using some formulas. If you go to url.py page you can see there is text in green above all your urls, there is path called : path('blog/', include('blog.urls')). Essentially this code will save some time if you have multiple apps within one website. When request comes to our website  its looking for url, and once its sees 'path/', its automatically forwards request to blog app.  

"	First we have to create new file for Blog urls. 
"	Go to Urls.py and add this path('blog/', include('blog.urls')) and copy all paths including with imported modules and libraries í right click on blog app and create Urls.py fileí paste all copied paths and modules, for this particular blog we only going to need few modules: 
                          from django.urls import path
                          from . import views

                         path('', views.all_blogs, name='all_blogs'),
                         path('<int:blog_id>/', views.detail, name='detail') 
 
"	int:blog_id refers to a number of the page we could display to user, let's say we have 4-5 blogs and user only wants to see blog3. So he/she can type localhost:8000/blog/3/ í this will display blog 3, rather than just displaying all blogs. Very important aspect when we create Detail Page, we need to import get_object_or_404, this way if your app has only 5 blogs, lets say user types localhost:8000/blog/6 it will display page not found message. 

"	After when you created detail function you will need create Model and Templates for our blogs, just like we did with first app. 

Once our both apps are good to go, we can add some Bootstraps to make our page look nicer. 
Below I going to display all steps I did while creating this project.  For NavBar you will need to copy HTML and JS code from www.getbootstrap.com . 
  
