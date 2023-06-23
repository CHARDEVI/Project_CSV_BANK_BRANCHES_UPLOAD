from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from cherry.models import *
import csv


def bank_upload(request):
            a='C:\\Users\\91789\\OneDrive\\Desktop\\74DE6\\devi\\Scripts\\projectcsv\\bank.csv'
            with open(a,'r') as file:
                  csv_data=csv.reader(file)
                  print(next(csv_data))
                  for a in csv_data:
                        bn=a[0].strip()
                        instance=Bank(BName=bn)
                        instance.save()


                  return HttpResponse("Bank Data is Inserted Successfully")
        


def branch_upload(request):
    a='C:\\Users\\91789\\OneDrive\\Desktop\\74DE6\\devi\\Scripts\\projectcsv\\branch1.csv'
    with open(a,'r') as file:
            csv_data=csv.reader(file)
            print(next(csv_data))

            for a in csv_data:
                bn=a[0].strip()
                bank_object=Bank.objects.get(BName=bn)
                instance=Branch(BName=bank_object,
                IFSC=a[1],
                BRANCH=a[2],
                ADDRESS=a[3],
                CONTACT=a[4],
                CITY=a[5],
                DISTRICT=a[6],
                STATE=a[7],)
                instance.save()


            return HttpResponse("Bank-Branches Data is Inserted Successfully")



'''

            
'''
