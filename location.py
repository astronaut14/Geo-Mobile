import phonenumbers
from test import number

from phonenumbers import geocoder
pn_nmber = phonenumbers.parse(number, "pn")
print(geocoder.description_for_number(pn_nmber, "en"))

from phonenumbers import carrier 
service_nmber = phonenumbers.parse(number, "PH")
print(carrier.name_for_number(service_nmber, "en"))

# Paste the mobile number in number.py file