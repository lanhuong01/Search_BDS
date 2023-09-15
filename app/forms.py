from django import forms
from django.forms import ModelForm
from .models import BDS

class BDSform(ModelForm):
	class Meta:
		model = BDS
		fields = ('news_type','price','size','direction','balcony_direction','legal','width','length','bedrooms','toilets','floors','furniture','url','location','description')
		# labels = {
		# 	'news_type':'news_type',
        #     'price': 'Price',
        #     'size': 'Size',
        #     'direction':'Direction',
        #     'balcony_direction': 'Balcony direction',
        #     'legal':'Legal',
        #     'width':'Width',
        #     'length':'Length',
        #     'bedrooms':'Bedrooms',
        #     'toilets':'Toilets',
        #     'floors':'Floors',
        #     'furniture':'Furniture',
        #     'url':'URL',
        #     'location':'Location',
        #     'description':'Description'	,	
		# }
		widgets = {
			'news_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'News type'}),
			'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
			'size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Size'}),
			'direction': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direction'}),
			'balcony_direction': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Balcony direction'}),
			'legal': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Legal'}),
            'width': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Width'}),
            'length': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Length'}),
            'bedrooms': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Bedrooms'}),
            'toilets': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Toilets'}),
            'floors': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Floors'}),
            'furniture': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Furniture'}),
            'url': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'URL'}),
            'location': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'description': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Description'}),
		}

