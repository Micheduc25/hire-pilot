import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from pdfminer.high_level import extract_text
from account.models import User


# Resume Model
class Resume(models.Model):
    name = models.CharField(max_length=20)
    resume = models.FileField(upload_to="Candidates/Documents")
    uploaded_at = models.DateTimeField(auto_now=True)


# Candidate model



# Employer Model


class Employer(models.Model):
    Agriculture = "Agriculture"
    Engineering = "Engineering"
    Health_Care = "Health Care"
    Hospitality_and_Tourism = "Hospitality and Tourism"
    Aerospace = "Aerospace"
    Transport_and_Logistics = "Transport and Logistics"
    Banking_and_Finance = "Banking and Finance"
    Media_and_Entertainement = "Media and Entertainment"
    Professional_Services = "Professional Services"
    Technology = "Technology"
    Others = "Others"

    industry_category = [
        (Agriculture, "Agriculture"),
        (Engineering, "Engineering"),
        (Health_Care, "Health Care"),
        (Hospitality_and_Tourism, "Hospitality and Tourism"),
        (Aerospace, "Aerospace"),
        (Transport_and_Logistics, "Transport and Logistics"),
        (Banking_and_Finance, "Banking and Finance"),
        (Media_and_Entertainement, "Media and Entertainment"),
        (Professional_Services, "Professional Services"),
        (Technology, "Technology"),
        (Others, "Others"),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=55)
    location = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    industry_type = models.CharField(
        max_length=25, choices=industry_category, default=Others
    )
    date_created = models.DateField("date created", default=timezone.now)

    def __str__(self):
        return self.company_name
# Skills

class Skills(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Degree(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
#  Job modelcompany


class Job(models.Model):
    Full_time = "Full Time"
    Part_time = "Part Time"

    fulltime_parttime = [
        (Full_time, "Full Time"),
        (Part_time, "Part Time"),
    ]

    Offline = "Offline"
    Remote = "Remote"

    offlineorremote = [
        (Offline, "Offline"),
        (Remote, "Remote"),
    ]

    One = 'One'
    Two = 'Two'

#   Applying authtoken.0003_tokenproxy... OK
    selectionstep = [
        (One, "One"),
        (Two, "Two")
    ]
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    fulltime_partime = models.CharField(
        max_length=10, choices=fulltime_parttime, default=Full_time
    )
    offline_remote = models.CharField(
        max_length=7, choices=offlineorremote, default=Offline
    )
    submission_deadline = models.DateField(max_length=30)
    selection_step = models.CharField(choices=selectionstep, default=One, max_length=15)
    salary_range = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    degree = models.ManyToManyField(Degree, related_name="jobs")
    language = models.ManyToManyField(Language, related_name="jobs")
    skills = models.ManyToManyField(Skills, related_name="jobs")
    date_created = models.DateField("date created", default=datetime.date.today)

    def __str__(self):
        return self.title



# Application model
class Apply(models.Model):
    Pending = "Pending"
    Interview = "Interview"
    Approved = "Approved"
    Declined = "Decline"

    status_choices = [  
        (Pending, "Pending"),
        (Interview, "Interview"),
        (Approved, "Approved"),
        (Declined, "Declined"),
    ]
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="Candidates/Documents", null=True, blank=True)
    candidate_extracted_data = models.JSONField(null=True, blank=True)
    status = models.CharField(
        max_length=9, choices=status_choices, default="Pending", blank=True
    )
    apply_date = models.DateField("apply date", default=timezone.now)

    def __str__(self):
        return self.candidate.username


# Selection
class Selection(models.Model):
    name_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
