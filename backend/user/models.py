from django.db import models
from django.conf import settings

def upload_image_field(instance,filename):
    # new_filename=random.randint(1,5446346843163)
    name,ext=get_file_ext(filename)
    finalname='{new_name}{ext}'.format(new_name=name,ext=ext)
    return 'media/profile/{username}/{new_filename}/{finalname}'.format(username=instance.user,new_filename=name,finalname=finalname)

class User (models.Model):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"
    OTHER = "o"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (OTHER, "Other"),
    )

    profile=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    mobile_number=models.PositiveIntegerField(blank=True, null=True)
    profile_img=models.ImageField(upload_to=upload_image_field, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    about = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.profile.username

class TimeStampedModel(models.Model):
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Address(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="address", on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default='Unknown')
    number=models.CharField(max_length=100,default='Unknown')
    city = models.CharField(max_length=100, blank=False, null=False)
    district = models.CharField(max_length=100, blank=False, null=False)
    street_address = models.CharField(max_length=250, blank=False, null=False)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    primary = models.BooleanField(default=False)
    phone_number=models.PositiveIntegerField(blank=True, null=True)
    building_number = models.PositiveIntegerField(blank=True, null=True)
    apartment_number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username