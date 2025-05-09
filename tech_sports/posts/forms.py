from .models import Post,Tag
from django import forms
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, Submit,HTML,Div


    



class PostForm(ModelForm):

    tags = forms.CharField(
    # queryset=Tag.objects.all(),
    # widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple
    widget = forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'}),
    required=False
    )
    class Meta:
        model = Post
        fields = ["title","content","tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create-Form'
        # css
       
        self.helper.form_class = 'createForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_post'
        # self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
            Div(
                Div(
            Fieldset(
                'Create New Post',
                'title',
                'content',
                'tags',
            
        # self.helper.add_input(Submit('submit', 'Submit'))
            ),Submit('submit', 'Submit', css_class='button white'),
                 css_class='col-md-6 p-4 bg-light rounded w-100'),
            css_class='d-flex justify-content-center align-items-center '
        )
        )

    def clean_tags(self):
        raw_tags = self.cleaned_data['tags']

        if raw_tags:
            tag_list =[x.strip() for x in raw_tags.split(',')]
            tags = []
            for tag_name in tag_list:
                tag,created = Tag.objects.get_or_create(title = tag_name)
                tags.append(tag)
            return tags
        return []




