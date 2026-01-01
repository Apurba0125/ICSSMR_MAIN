
import os

def student_upload_path(instance, filename):
    # Safe folder name
    name = instance.name.replace(" ", "_")
    mobile = instance.mobile

    # Folder: Students/Name-Mobile/
    folder_name = f"Students/{name}-{mobile}"

    return os.path.join(folder_name, filename)



#student membership 
import os
from django.utils.text import slugify

def student_upload_path(instance, filename):
    name = slugify(instance.name)
    mobile = instance.mobile
    folder_name = f"{name}-{mobile}"

    return os.path.join(
        "Student Membership",
        folder_name,
        filename
    )

