from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, Submit,HTML,Div

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username","password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

    
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                'User Registration',
                'username',
                'password1',
        #             HTML("""
        #     <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
        # """),
                'password2',
            Submit('submit', 'Submit', css_class='button white'),
            ),
        # self.helper.add_input(Submit('submit', 'Submit'))
        )


