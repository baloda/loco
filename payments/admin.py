from django.contrib import admin

# Register your models here.
from payments.models import Transactions

admin.site.register(Transactions)