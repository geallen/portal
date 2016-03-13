from django.contrib.auth.forms import UserCreationForm

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import MyUser, Post

class RegistrationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields =  ('username','email','date_of_birth',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            'email',
            'date_of_birth',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message',)

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'message',

            ButtonHolder(
                Submit('post_edit', 'Done', css_class='btn-success')
            )
        )
