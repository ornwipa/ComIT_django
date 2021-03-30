from django import forms
from django.core.exceptions import ValidationError
from people.models import Person # gateway to database

class FirstNameForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()

    def clean_first_name(self): # can't accept any value
        """ Custom clean method following the pattern clean_<FIELD NAME>
            Raise ValidationError to add error message.
            Return cleaned field value if there is no error.
        """

        if self.cleaned_data['first_name'] == 'Steve':
            raise ValidationError('Steve is a terrible name.')

        return self.cleaned_data['first_name'] # must return something

    def clean_email(self): # check for email duplication
        email = self.cleaned_data['email'] # get email from cleaned_data attribute        
        person_count = Person.objects.filter(email=email).count() # query database
        
        if person_count == 0:
            return email
        else:
            raise ValidationError('A person with this email already exists.')

    def clean(self):
        return self.cleaned_data
