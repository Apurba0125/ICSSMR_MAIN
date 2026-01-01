from decimal import Decimal
from django.shortcuts import render,redirect
from .models import StudentRegistration
from .models import AssociateMembership
from .models import FacultyMembership



def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def notice(request):
    return render(request, 'notice.html')


def course(request):
    return render(request, 'course.html')





# student data form data save part

def stu_registration(request):
    if request.method == "POST":

        StudentRegistration.objects.create(
            # -------- Personal Information --------
            name=request.POST.get('name'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),

            # -------- Contact Information --------
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            whatsapp=request.POST.get('whatsapp'),

            # -------- Qualification & Course --------
            qualification=request.POST.get('qualification'),
            course=request.POST.get('course'),

            # -------- Address --------
            address1=request.POST.get('address1'),
            address2=request.POST.get('address2'),
            city=request.POST.get('city'),
            district=request.POST.get('district'),
            state=request.POST.get('state'),
            country=request.POST.get('country'),
            pin=request.POST.get('pin'),

            # -------- Academic Marks --------
           marks_10=Decimal(request.POST.get("marks_10")),
            marks_12=Decimal(request.POST.get("marks_12")),
            marks_ug=Decimal(request.POST.get("marks_ug")),
            marks_pg=Decimal(request.POST.get("marks_pg")) if request.POST.get("marks_pg") else None,

            # -------- Uploaded Documents --------
            ug_marksheet=request.FILES.get('ug_marksheet'),
            x_admit=request.FILES.get('x_admit'),
            x_marksheet=request.FILES.get('x_marksheet'),
            xii_marksheet=request.FILES.get('xii_marksheet'),
            aadhar=request.FILES.get('aadhar'),
            cv=request.FILES.get('cv'),
            photo=request.FILES.get('photo'),
        )

        return redirect('payment')  # change if needed

    return render(request, 'stu_registration.html')




def vision_mission(request):
    return render(request, 'vm.html')


def membership(request):
    return render(request, 'membership.html')


#faculty membership 

def faculty_membershipform(request):
    if request.method == "POST":

        # Collect multiple specialization values
        specialization_list = request.POST.getlist("specialization")

        # Save data to database
        FacultyMembership.objects.create(
            salutation=request.POST.get("salutation"),
            name=request.POST.get("name"),
            dob=request.POST.get("dob"),
            gender=request.POST.get("gender"),

            email=request.POST.get("email"),
            mobile=request.POST.get("mobile"),
            whatsapp=request.POST.get("whatsapp"),

            institution=request.POST.get("institution"),
            experience=request.POST.get("experience"),
            designation=request.POST.get("designation"),
            qualification=request.POST.get("qualification"),

            domain=request.POST.get("domain"),
            specialization=", ".join(specialization_list),

            research_interest=request.POST.get("researchInterest"),

            address1=request.POST.get("address1"),
            address2=request.POST.get("address2"),
            city=request.POST.get("city"),
            district=request.POST.get("district"),
            state=request.POST.get("state"),
            country=request.POST.get("country"),
            pin=request.POST.get("pin"),

            aadhar=request.FILES.get("aadhar"),
            id_card=request.FILES.get("idCard"),
            cv=request.FILES.get("cv"),
            photo=request.FILES.get("photo"),
        )

        return redirect("payment")  # create success page url

    return render(request, 'faculty_membershipform.html')
    


# associate membership 
def associate_membershipform(request):
    if request.method == "POST":

        AssociateMembership.objects.create(
            # ---------- Personal Information ----------
            salutation=request.POST.get('salutation'),
            name=request.POST.get('name'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),

            # ---------- Contact Information ----------
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            whatsapp=request.POST.get('whatsapp'),

            # ---------- Professional Information ----------
            organization=request.POST.get('organization'),
            designation=request.POST.get('designation'),
            experience=request.POST.get('experience'),
            sector=request.POST.get('sector'),
            qualification=request.POST.get('qualification'),

            # ---------- Address ----------
            address1=request.POST.get('address1'),
            address2=request.POST.get('address2'),
            city=request.POST.get('city'),
            district=request.POST.get('district'),
            state=request.POST.get('state'),
            country=request.POST.get('country'),
            pin=request.POST.get('pin'),

            # ---------- Uploaded Files ----------
            aadhar=request.FILES.get('aadhar'),
            office_id=request.FILES.get('officeId'),
            cv=request.FILES.get('cv'),
            photo=request.FILES.get('photo'),
        )

        return redirect('payment')  # change if needed

    return render(request, 'associate_membershipform.html')




# student membership
from django.shortcuts import render, redirect
from .models import StudentMembership

def stu_membershipform(request):
    if request.method == "POST":

        # collect multiple checkbox values
        domains = request.POST.getlist('domain')
        domain_str = ", ".join(domains)

        StudentMembership.objects.create(
            # Personal Information
            name=request.POST.get('name'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),

            # Contact Information
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            whatsapp=request.POST.get('whatsapp'),

            # Address
            address1=request.POST.get('address1'),
            address2=request.POST.get('address2'),
            city=request.POST.get('city'),
            district=request.POST.get('district'),
            state=request.POST.get('state'),
            country=request.POST.get('country'),
            pin=request.POST.get('pin'),

            # Education
            qualification=request.POST.get('qualification'),
            marks10=request.POST.get('marks10'),
            marks12=request.POST.get('marks12'),
            marksUG=request.POST.get('marksUG'),
            marksPG=request.POST.get('marksPG') or None,

            # Internship
            internship=request.POST.get('internship'),
            domain=domain_str if request.POST.get('internship') == 'Yes' else '',

            # Files
            aadhar=request.FILES.get('aadhar'),
            collegeid=request.FILES.get('collegeid'),
            cv=request.FILES.get('cv'),
            photo=request.FILES.get('photo'),
        )

        return redirect('payment')  # or success page

    return render(request, 'stu_membershipform.html')










def PGCBA(request):
    return render(request, 'PGCBA.html')


def PGCHM(request):
    return render(request, 'PGCHM.html')

def PGCHRM(request):
    return render(request, 'PGCHRM.html')

def PGCBIM(request):
    return render(request, 'PGCBIM.html')

def contact(request):
    return render(request, 'contact.html')



def payment(request):
    return render(request, 'payment.html')








# publication part

def pub_home(request):
    return render(request, 'pub_home.html')

def pub_aboutus(request):
    return render(request, 'pub_aboutus.html')

def pub_aim(request):
    return render(request, 'pub_aim.html')

def pub_openaccess(request):
    return render(request, 'pub_openaccess.html')

def pub_authorguidline(request):
    return render(request, 'pub_authorguidline.html')


def pub_ethics(request):
    return render(request, 'pub_ethics.html')

def pub_privacystatement(request):
    return render(request, 'pub_privacystatement.html')

def pub_patron(request):
    return render(request, 'pub_patron.html')

def pub_editors(request):
    return render(request, 'pub_editors.html')

def pub_journalcordinates(request):
    return render(request, 'pub_journalcordinates.html')

def pub_issues(request):
    return render(request, 'pub_issues.html')


def pub_contact(request):
    return render(request, 'pub_contact.html')



# bulk mail send script
# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
import threading

def send_email_thread(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            None,  # From email (uses DEFAULT_FROM_EMAIL)
            recipient_list,
            fail_silently=False,
            html_message=message  # If using HTML content
        )
    except BadHeaderError:
        print("Invalid header found.")
    except Exception as e:
        print(f"Error sending email: {e}")

def bulk_mail(request):
    if request.method == 'POST':
        emails = request.POST.getlist('emails[]')  # List of emails from dynamic inputs
        subject = request.POST.get('subject', 'Greetings from Admin')
        message = request.POST.get('message', 'Hello! This is a predefined email.')

        # Filter out empty emails
        emails = [e for e in emails if e.strip()]

        if not emails:
            messages.error(request, "No email addresses provided.")
            return redirect('bulk_mail')

        # Send emails in a separate thread
        thread = threading.Thread(target=send_email_thread, args=(subject, message, emails))
        thread.start()

        messages.success(request, f"Emails are being sent to {len(emails)} recipients.")
        return redirect('bulk_mail')

    return render(request, 'bulk_mail.html')
