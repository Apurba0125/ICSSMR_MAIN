from django.db import models
import os


def student_upload_path(instance, filename):
    # Safe folder name
    name = instance.name.replace(" ", "_")
    mobile = instance.mobile

    # Folder: Students/Name-Mobile/
    folder_name = f"Students/{name}-{mobile}"

    return os.path.join(folder_name, filename)


class StudentRegistration(models.Model):

    # ---------- Personal Information ----------
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ]
    )

    # ---------- Contact Information ----------
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)

    # ---------- Qualification ----------
    qualification = models.CharField(max_length=100)

    # ---------- Course Selection ----------
    course = models.CharField(max_length=200)

    # ---------- Address ----------
    address1 = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    pin = models.CharField(max_length=10)

    # ---------- Academic Marks ----------
    marks_10 = models.DecimalField(max_digits=5, decimal_places=2)
    marks_12 = models.DecimalField(max_digits=5, decimal_places=2)
    marks_ug = models.DecimalField(max_digits=5, decimal_places=2)
    marks_pg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    # ---------- Documents ----------
    ug_marksheet = models.FileField(upload_to=student_upload_path)
    x_admit = models.FileField(upload_to=student_upload_path)
    x_marksheet = models.FileField(upload_to=student_upload_path)
    xii_marksheet = models.FileField(upload_to=student_upload_path)
    aadhar = models.FileField(upload_to=student_upload_path)
    cv = models.FileField(upload_to=student_upload_path)
    photo = models.ImageField(upload_to=student_upload_path)

    # ---------- Meta ----------
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"







# bulk mail send

from django.db import models

class BulkMail(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipient_email






# associate membership form
from django.db import models
import os

def associate_upload_path(instance, filename):
    # Folder name: Associate Membership/Name-Mobile/
    safe_name = instance.name.replace(" ", "_")
    folder_name = f"Associate Membership/{safe_name}-{instance.mobile}"
    return os.path.join(folder_name, filename)


class AssociateMembership(models.Model):

    # ---------------- Personal Information ----------------
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

    # ---------------- Contact Information ----------------
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)

    # ---------------- Professional Information ----------------
    organization = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    sector = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    # ---------------- Address Information ----------------
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    pin = models.CharField(max_length=10)

    # ---------------- Documents ----------------
    aadhar = models.FileField(upload_to=associate_upload_path)
    office_id = models.FileField(upload_to=associate_upload_path)
    cv = models.FileField(upload_to=associate_upload_path)
    photo = models.ImageField(upload_to=associate_upload_path)

    # ---------------- Meta ----------------
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"




#faculty membership 
from django.db import models
import os


def faculty_upload_path(instance, filename):
    # Folder: Faculty Membership/Name-Mobile/
    folder_name = f"{instance.name}-{instance.mobile}"
    return os.path.join("Faculty Membership", folder_name, filename)


class FacultyMembership(models.Model):

    # ---------- Personal Info ----------
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

    # ---------- Contact Info ----------
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)

    # ---------- Professional Info ----------
    institution = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)

    # ---------- Domain & Specialization ----------
    domain = models.CharField(max_length=50)
    specialization = models.TextField()  # stored as comma-separated

    # ---------- Research ----------
    research_interest = models.TextField()

    # ---------- Address ----------
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)

    # ---------- Documents ----------
    aadhar = models.FileField(upload_to=faculty_upload_path)
    id_card = models.FileField(upload_to=faculty_upload_path)
    cv = models.FileField(upload_to=faculty_upload_path)
    photo = models.ImageField(upload_to=faculty_upload_path)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"

#student membership
from django.db import models
from .utils import student_upload_path

class StudentMembership(models.Model):

    # Personal Information
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

    # Contact Information
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)

    # Address
    address1 = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    pin = models.CharField(max_length=10)

    # Education
    qualification = models.CharField(max_length=50)
    marks10 = models.DecimalField(max_digits=5, decimal_places=2)
    marks12 = models.DecimalField(max_digits=5, decimal_places=2)
    marksUG = models.DecimalField(max_digits=5, decimal_places=2)
    marksPG = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # Internship
    internship = models.CharField(max_length=10)
    domain = models.CharField(max_length=200, blank=True, null=True)

    # Documents
    aadhar = models.FileField(upload_to=student_upload_path)
    collegeid = models.FileField(upload_to=student_upload_path)
    cv = models.FileField(upload_to=student_upload_path)
    photo = models.ImageField(upload_to=student_upload_path)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"
