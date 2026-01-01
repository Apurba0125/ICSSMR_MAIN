"""icssmrProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('notice/', views.notice, name='notice'),
    path('course/', views.course, name='course'),
    path('vision_mission/', views.vision_mission, name='vision_mission'),
    path('membership/', views.membership, name='membership'),
    path('stu_membershipform/', views.stu_membershipform, name='stu_membershipform'),
    path('faculty_membershipform/', views.faculty_membershipform, name='faculty_membershipform'),
    path('associate_membershipform/', views.associate_membershipform, name='associate_membershipform'),
    path('PGCBA/', views.PGCBA, name='PGCBA'),
    path('PGCHM/', views.PGCHM, name='PGCHM'),
    path('PGCHRM/', views.PGCHRM, name='PGCHRM'),
    path('PGCBIM/', views.PGCBIM, name='PGCBIM'),
    path('contact/', views.contact, name='contact'),
    path('payment/', views.payment, name='payment'),
    path('stu_registration/', views.stu_registration, name='stu_registration'),
    path('pub_home/', views.pub_home, name='pub_home'),
    path('pub_aboutus/', views.pub_aboutus, name='pub_aboutus'),
    path('pub_aim/', views.pub_aim, name='pub_aim'),
    path('pub_openaccess/', views.pub_openaccess, name='pub_openaccess'),
    path('pub_contact/', views.pub_contact, name='pub_contact'),
    path('pub_ethics/', views.pub_ethics, name='pub_ethics'),
    path('pub_privacystatement/', views.pub_privacystatement, name='pub_privacystatement'),
    path('pub_patron/', views.pub_patron, name='pub_patron'),
    path('pub_editors/', views.pub_editors, name='pub_editors'),
    path('pub_journalcordinates/', views.pub_journalcordinates, name='pub_journalcordinates'),
    path('pub_issues/', views.pub_issues, name='pub_issues'),
    path('pub_authorguidline/', views.pub_authorguidline, name='pub_authorguidline'),

    
    path('bulk-mail/', views.bulk_mail, name='bulk_mail'),






 
]




