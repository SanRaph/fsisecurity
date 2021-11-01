from django.db import models

# Create your models here.

# "Email": "usert@dummydata.com",
# 	"PhoneNumber": "+234(0)8031121190",
# 	"Salutation": "MRS.",
# 	"FirstName": "Mia",
# 	"MiddleName": "Afit",
# 	"LastName": "Okai",
# 	"Gender": "M",
# 	"DOB": "1976-12-01",
# 	"Address" : "Ikot Ntuen",
# 	"MaritalStatus": "MRIED",
# 	"BVN" : "22121122222",
# 	"APPID" : "Dukia Gold"

GENDER = (
    ('f', 'F'),
    ('m', 'M'),
)

MARITALSTATUS = (
    ('single', 'SINGLE'),
    ('married', 'MARRIED'),
)

SALUTATION = (
    ('mr', 'MR'),
    ('mrs', 'MRS'),
)

CURRENCY = (
    ('ngn', 'NGN'),
    ('usd', 'USD'),
)


class Account(models.Model):
    Email = models.EmailField(max_length=225, blank=False)
    PhoneNumber = models.CharField(max_length=225, blank=False)
    Salutation = models.CharField(max_length=225, choices=SALUTATION, blank=False)
    FirstName = models.CharField(max_length=225, blank=False)
    MiddleName = models.CharField(max_length=225, blank=False)
    LastName = models.CharField(max_length=225, blank=False)
    Gender = models.CharField(max_length=225, choices=GENDER, blank=False)
    DOB = models.CharField(max_length=225, blank=False)
    Address = models.CharField(max_length=225, blank=False)
    MaritalStatus = models.CharField(max_length=225, choices=MARITALSTATUS, blank=False)
    BVN = models.CharField(max_length=225, blank=False)
    APPID = models.CharField(max_length=225, blank=True)


class Transfer(models.Model):
    Amount = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    DebitAccount = models.CharField(max_length=225, blank=False)
    CreditAccount = models.CharField(max_length=225, blank=False)
    Narration = models.CharField(max_length=225, blank=False)
    Fee = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    ValueDate = models.CharField(max_length=225, blank=False)
    TransactionReference = models.CharField(max_length=225, blank=False)
    Currency = models.CharField(max_length=225, choices=CURRENCY, blank=False)

