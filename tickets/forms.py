from django import forms

class CreateTicketForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label="Title", min_length=5)
    description = forms.CharField(required=True, label="Description", min_length=5)
    category_id = forms.IntegerField(required=True, label="Category")
    department_id = forms.IntegerField(required=True, label="Department")