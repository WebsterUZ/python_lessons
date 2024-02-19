import phonenumbers
from phonenumbers import geocoder

Phone_Number1 = phonenumbers.parse("+998904880119")
Number_n1 = phonenumbers.parse("904880119", "GB")



print("\nPhone Number Location:")

print(geocoder.description_for_number(Phone_Number1,"en"))
print(Number_n1)
