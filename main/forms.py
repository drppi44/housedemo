from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from main.models import Flat, House


class FlatForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_id = 'id_flat'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    class Meta:
        model = Flat
        exclude = ('created',)


class HouseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_id = 'id_house'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    class Meta:
        model = House
        exclude = ('created',)
