from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Lecture

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        '''Widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'middle_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'degree':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileField(attrs={'class':'form-control'})
        }'''
     

    def __init__(self,*args, **kwargs):
       
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['middle_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        #self.fields['ranking'].widget.attrs['class'] = 'form-control'
        #self.fields['profession'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        #self.fields['shift'].widget.attrs['class'] = 'form-control'     '''
class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = "__all__"
    def __init__(self,*args, **kwargs):
       
        super(LectureForm, self).__init__(*args, **kwargs)