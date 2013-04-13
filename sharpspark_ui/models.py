from django.core.urlresolvers import reverse
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class View(models.Model):
    """Describes a View"""
    name = models.TextField(name="name", verbose_name="View Name", null=False, unique=True)

class FillableInterface(models.Model):
    """Block of text by name to be created"""
    tag = models.TextField(name="fieldtag", unique=True)
    view = models.ForeignKey(View)
    content = models.SlugField(name="content", null=False)
    updated = models.DateTimeField(name="updated", verbose_name="Updated At", auto_now=True)

class LearningOutcome(models.Model):
    """Learning Outcome for a Course"""
    name = models.TextField(name="name", null=False)
    description = models.TextField(name="description", verbose_name="Learning Outcome")

class KeyWord(models.Model):
    keyword = models.TextField(name="keyword", verbose_name="Course Keyword")

class Course(models.Model):
    """Course for students"""
    name = models.TextField(name="name", verbose_name="Course Name", null=False, unique=True)
    description = models.TextField(name="description", verbose_name="Course Description")
    learning_outcomes = models.ManyToManyField(LearningOutcome)
    keywords = models.ManyToManyField(KeyWord)

class Contact(models.Model):
    """Contact Request"""
    # Interest Modalities
    ENROLL = 0
    MOREINFO = 1
    LICENSING = 2
    INTEREST_AREA = (
        (ENROLL, "Enrolling in a course"),
        (MOREINFO, "More info on Sharp Spark"),
        (LICENSING, "Taking Sharp Spark global (mwhahahah)")
    )
    # Contact Modalities
    PHONE = 0
    EMAIL = 1
    FAX = 2
    CONTACT_MODES = (
        (PHONE, "Phone"),
        (EMAIL, "Email"),
        (FAX, "Fax (you're kidding, right?)")
    )
    date = models.DateTimeField(name="contactdate", verbose_name="Date of Contact", auto_now_add=True)
    name = models.CharField(name="contactname",
                            verbose_name="Name",
                            null=False,
                            max_length=100)
    email = models.EmailField(name="contactemail", verbose_name="Email Address")
    contact_number = PhoneNumberField(name="contact_number", verbose_name="Phone Number")
    area_of_interest = models.IntegerField(name="area_of_interest",
                                        verbose_name="What are you mostly interested in?",
                                        max_length=2,
                                        choices=INTEREST_AREA,
                                        default=ENROLL,
                                        null=False)
    primary_mode = models.IntegerField(name="preferred_contact",
                                       verbose_name="Preferred contact method?",
                                       choices=CONTACT_MODES,
                                       default=EMAIL,
                                       null=False)
    comments = models.TextField(name="comments",
                                verbose_name="Any information that can help us, help you?")


    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk': self.pk})