from django.core.urlresolvers import reverse
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class View(models.Model):
    """Describes a View"""
    name = models.CharField(name="name",
                            verbose_name="View Name",
                            null=False,
                            unique=True,
                            max_length=100)

class FillableInterface(models.Model):
    """Block of text by name to be created - for wiki'ised updates"""
    tag = models.CharField(name="fieldtag",
                           unique=True,
                           max_length=15)
    view = models.ForeignKey(View)
    content = models.SlugField(name="content", null=False)
    updated = models.DateTimeField(name="updated", verbose_name="Updated At", auto_now=True)

class LearningOutcome(models.Model):
    """Learning Outcome for a Course"""
    name = models.TextField(name="name", null=False)
    description = models.TextField(name="description", verbose_name="Learning Outcome")

class KeyWord(models.Model):
    """Stack of categories for a course"""
    keyword = models.TextField(name="keyword", verbose_name="Course Keyword")

class Course(models.Model):
    """Course for students"""
    name = models.CharField(name="name",
                            verbose_name="Course Name",
                            null=False,
                            unique=True,
                            max_length=250)
    description = models.CharField(name="description",
                                   verbose_name="Course Description",
                                   max_length=250)
    learning_outcomes = models.ManyToManyField(LearningOutcome)
    keywords = models.ManyToManyField(KeyWord)

class Student(models.Model):
    """Student for a course"""
    surname = models.CharField(name="surname",
                               verbose_name="Student Surname",
                               max_length=100,
                               null=False)
    forename = models.CharField(name="forename",
                                verbose_name="Student Forename",
                                max_length=100,
                                null=False)
    dob = models.DateField(name="dob", verbose_name="Date of Birth")
    first_contact = models.DateField(name="first_contact", verbose_name="Date of First Contact",
                                     auto_now_add=True, null=False)

class ResponsibleAdult(models.Model):
    """Responsible Adult"""
    surname = models.CharField(name="surname",
                               verbose_name="Responsible Adult Surname",
                               null=False,
                               max_length=100)
    forename = models.CharField(name="forename",
                                verbose_name="Responsible Adult Forename",
                                null=False,
                                max_length=100)
    contact_number = PhoneNumberField(null=False)
    email = models.EmailField(verbose_name="Responsible Adult Email")

class StudentLink(models.Model):
    """Links a Student to an Adult"""
    adult = models.ManyToManyField(ResponsibleAdult)
    student = models.ForeignKey(Student)


class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    date = models.DateField(verbose_name="Date of Enrollment")

class CourseConduct(models.Model):
    """Invocation of course"""
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    start_date = models.DateField(verbose_name="Start Date for Course")
    end_date = models.DateField(verbose_name="End Date for Course")
    outcome = models.IntegerField(verbose_name="Outcome of Course",
                                  choices=((1, 'Started'),
                                           (2, 'Completed'),
                                           (3, "Pulled out")),
                                  )

class CourseLocation(models.Model):
    contact_number = PhoneNumberField(verbose_name="Contact phone number")
    # TODO: Store as a blob, but should hve a more 'aware' field
    text_address = models.TextField(verbose_name="Address")

class ContactRequest(models.Model):
    """Contact Request from the website"""
    # Interest Modalities
    INTEREST_AREA = (
        (0, "Enrolling in a course"),
        (1, "More info on Sharp Spark"),
        (2, "Arranging a Course in your School"),
        (3, "Tutoring (Chemistry, General Science)"),
        (4, "Tutoring (Exam Skills)"),

    )
    # Contact Modalities
    CONTACT_MODES = (
        (0, "Phone"),
        (1, "Email"),
        (2, "Fax (you're kidding, right?)")
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
                                        default=0,
                                        null=False)
    primary_mode = models.IntegerField(name="preferred_contact",
                                       verbose_name="Preferred contact method?",
                                       choices=CONTACT_MODES,
                                       default=1,
                                       null=False)
    comments = models.CharField(name="comments",
                                verbose_name="Any information that can help us, help you?",
                                max_length=500)


    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk': self.pk})