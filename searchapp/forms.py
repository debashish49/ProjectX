from django import forms

class searchform(forms.Form):
    search = forms.CharField(label="")

class pricefilter(forms.Form):
    choices = forms.ChoiceField(choices=[('','Filter by Price'),('desc','High to Low'),('asc','Low to High')],label="", required=False)

class retailerfilter_laptop(forms.Form):
    retailer = forms.ChoiceField(choices=[('','Filter by Retailer'),('kakaku','Kakaku'),('biccamera','Biccamera'),('nojima','Nojima'),('yodobashi','Yodobashi'),('yamada-denkiweb','Yamada Denki')],label="", required=False)

class retailerfilter_phones(forms.Form):
    retailer = forms.ChoiceField(choices=[('','Filter by Retailer'),('rakuten','Rakuten'),('apple.com','Apple'),('yamada-denkiweb','Yamadadenki'),('biccamera','Biccamera'),('yodobashi','Yodobashi')],label="", required=False)

class signupform(forms.Form):
    username = forms.CharField(label="Username:", max_length=25, required=True)
    firstname = forms.CharField(label="First Name:", max_length=25, required=True)
    lastname = forms.CharField(label="Last Name:", max_length=25, required=True)
    password = forms.CharField(label="Password:", widget = forms.PasswordInput())
    repassword = forms.CharField(label="Confirm Password:", widget = forms.PasswordInput())

class loginform(forms.Form):
    username = forms.CharField(label="Username:", max_length=25, required=True)
    password = forms.CharField(label="Password:", widget = forms.PasswordInput())