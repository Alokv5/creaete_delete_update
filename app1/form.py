from django import forms
from app1.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model =Product
        fields= "__all__"

    quantity=forms.IntegerField(min_value=1)

    def clean_price(self):
        price=self.cleaned_data["price"]
        if price>=10000:
            return price
        else:
            raise forms.ValidationError("Invalid Price")

