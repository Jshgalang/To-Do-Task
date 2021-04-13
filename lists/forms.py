from django import forms
from lists.models import Item

# class ItemForm(forms.Form):
	# item_text = forms.CharField(widget=forms.fields.TextInput(attrs={'placeholder':'Enter a to-do item', 'class': 'form-control input-lg'}),)


class ItemForm(forms.models.ModelForm):
	class Meta:
		model = item_text
		fields = ('text',)

