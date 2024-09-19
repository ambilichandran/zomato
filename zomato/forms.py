from django import forms
from .models import Detail
from django .forms import TextInput,Textarea
class Detailsform(forms.ModelForm):
    class Meta:
        model=Detail
        fields=['name','address','phone','email']
        widgets={
            'name':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"type your name"
                }
            ),
            'address':Textarea(
                attrs={
                    "type":"text",
                    "class":"form-control", 
                    "placeholder":"type your address"
                }
            ),
            'phone':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",  
                    "placeholder":"phone number"
                }
            ),
            'email':TextInput(
                attrs={
                    "type":"email", 
                    "class":"form-control", 
                "placeholder":"type your email"
                }
            )
        }
        
            
        
