from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanyRecords(models.Model):
    uuid_field = models.CharField(db_column='uuid_', primary_key=True,
                                  max_length=75)  # Field renamed because it ended with '_'.
    cin = models.CharField(max_length=21, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    busniess_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    no_of_employees = models.IntegerField(blank=True, null=True)
    employee_range = models.CharField(max_length=100, blank=True, null=True)
    legal_status = models.CharField(max_length=50, blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    turnover_range = models.CharField(max_length=100, blank=True, null=True)
    emails = models.CharField(max_length=200, blank=True, null=True)
    phones = models.CharField(max_length=150, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    incorporation_date = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    gsts = models.CharField(max_length=500, blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    modifiedby = models.CharField(max_length=75, blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    extra = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_records'


class LinkedinTextDb(models.Model):
    a = models.CharField(max_length=300, blank=True, null=True)
    liid = models.CharField(max_length=150, blank=True, null=True)
    e = models.CharField(max_length=400, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    t = models.CharField(max_length=300, blank=True, null=True)
    n = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_text_db'


class PersonRecords(models.Model):
    uuid_field = models.CharField(db_column='uuid_', max_length=75)  # Field renamed because it ended with '_'.
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=75, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    phone_numbers = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    company_website = models.CharField(max_length=200, blank=True, null=True)
    company_revenue = models.IntegerField(blank=True, null=True)
    company_revenue_range = models.CharField(max_length=100, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    employee_range = models.CharField(max_length=100, blank=True, null=True)
    extra_info = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_records'

    class DataStorage(models.Model):
        title = models.CharField(max_length=80, blank=True, null=True)
        full_address = models.TextField(blank=True, null=True)
        area = models.TextField(blank=True, null=True)  # district
        address1 = models.TextField(blank=True, null=True)
        city = models.CharField(max_length=30, blank=True, null=True)
        state = models.CharField(max_length=30, blank=True, null=True)
        pincode = models.CharField(max_length=10, blank=True, null=True)
        country = models.CharField(max_length=30, blank=True, null=True)
        phone_number = models.CharField(max_length=30, blank=True, null=True)
        place_type = models.TextField(blank=True, null=True)
        industry = models.CharField(max_length=30, blank=True, null=True)
        website = models.CharField(max_length=50, blank=True, null=True)
        social_links = models.TextField(blank=True, null=True)
        price_range = models.CharField(max_length=30, blank=True, null=True)
        timing = models.TextField(blank=True, null=True)
        thumbnail = models.TextField(blank=True, null=True)

        latitude = models.CharField(max_length=30, blank=True, null=True)
        longitude = models.CharField(max_length=30, blank=True, null=True)

        google_place_id = models.CharField(max_length=30, blank=True, null=True)
        place_link = models.CharField(max_length=30, blank=True, null=True)
        cid = models.CharField(max_length=30, blank=True, null=True)
        reviews_link = models.TextField(blank=True, null=True)
        booking_link = models.TextField(blank=True, null=True)
        place_id = models.TextField(blank=True, null=True)
        global_plus_code = models.CharField(max_length=30, blank=True, null=True)
        compound_plus_code = models.CharField(max_length=30, blank=True, null=True)

        review_count = models.CharField(max_length=5, blank=True, null=True)
        rating = models.CharField(max_length=5, blank=True, null=True)

        createdate = models.DateTimeField(blank=True, null=True)
        modifieddate = models.DateTimeField(blank=True, null=True)
