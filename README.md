# comicBackend 

A full-stack web application to read manga and manhwa with **real-time group chat** functionality.  
Users can log in, join manga-specific groups, and chat while reading.

#Live/Demo
 [View Live Project]/(https://reetish-bookstore.vercel.app)

 ## 🛠️ Tech Stack
**Frontend:** React, TailwindCSS  
**Backend:** Django, Django REST Framework, Django Channels  
**Database:** PostgreSQL  
**Deployment:** Vercel (frontend), Render (backend)


##Installation (Local setup)

initialize git by typing 'git init' in terminal
git clone https://github.com/REE-TISH/comicBackend.git
cd comicBackend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


##Additional change 
if you want to add your personal DATABASE then you could pass the DATABASE_URL otherwise you could use default sqllite3 database by replacing DATABASE in settings.py in comicBackend By this :
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }





