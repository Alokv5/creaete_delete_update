from django.shortcuts import render
from app1.models import  Product
from django.http import HttpResponse
from django.views.generic import View
from app1.form import ProductForm
import json
class insert_one(View):
    def post(self,request):
        data=request.body 
        dict_data= json.loads(data)
        pf=ProductForm(dict_data) 
        if pf.is_valid():
            pf.save()
            json_da=json.dumps({"Message":"Product is saved"})
        else:
            json_da=json.dumps({"error":pf.errors})
        return HttpResponse(json_da,content_type="application/json")



class delete_one(View):
    def get(self,request,product_no):
        try:
            result=Product.objects.get(pno=product_no)
            result.delete()
            json_data=json.dumps({"message":"Product  deleted"})

        except :
            json_data=json.dumps({"error":"Product no is invalid"})
        return HttpResponse(json_data,content_type="application/json")

class update_one(View):
    def put(self,request,product_no):
       try:
            old_product=Product.objects.get(pno=product_no)
            new_product=json.loads(request.body)
            data={
                "pno":old_product.pno,
                "name":old_product.name,
                "quantity":old_product.quantity,
                "maf_date":old_product.maf_date,
                "exp_date":old_product.exp_date

            }
            for key,value in new_product.items():
                data[key]=value

            pf=ProductForm(data,instance=old_product)
            if pf.is_valid():
                pf.save()
                json_data=json.dumps({"success":"Product is updated"})
            else:
                json_data=json.dumps(pf.errors)
            return HttpResponse(json_data,content_type="application/json")
       except Product.DoesNotExist:
            json_data=json.dumps({"error":"Invalid Product No."})
            return HttpResponse(json_data,content_type="application")
