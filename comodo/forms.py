from django.contrib.auth.forms import UserCreationForm, User

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div
from .models import MyUser, Post
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistrationsForm(RegistrationForm):

    email = forms.EmailField(required = True)
    city = forms.CharField(max_length=129)
    # user_status = forms.ChoiceField(choices=MyUser.USER_STATUS_DICT, widget=forms.RadioSelect)

    class Meta:
        model = MyUser
        fields = ('username','email', 'city','user_status',)

        # def __init__(self, *args, **kwargs):
        #     super(RegistrationForm, self).__init__(*args, **kwargs)

            # self.helper = FormHelper()
            # self.helper.field_class = 'form-control'
            # self.helper.layout = Layout(
            #     # 'username',
            #     # 'password1',
            #     # 'password2',
            #     # 'email',
            #     # 'city',
            #     #
            #     #
            #     #  InlineField('username', placeholder="Kullanici Adi",style="text-align: center;"),
            #     # InlineField('password1', placeholder="Confirm Password",style="text-align: center;"),
            #     # InlineField('password2', placeholder="Password",style="text-align: center;"),
            #     # InlineField('email', placeholder="Email",style="text-align: center;"),
            #     # InlineField('city', placeholder="Sehir",style="text-align: center;"),
            #     # ButtonHolder(
            #     #     Submit('register', 'Kayit Ol', css_class='btn btn-primary')
            #     # ),
            #
            # )

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.city = self.cleaned_data['city']
    #
    #     if commit:
    #         user.save()
    #     return user


    # address = forms.CharField(widget=forms.Textarea)
    # phone_number = forms.IntegerField()
    #
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'username',
    #         'password1',
    #         'password2',
    #         'email',
    #         'city',
    #         # ButtonHolder(
    #         #     Submit('register', 'Kayit Ol', css_class='btn-primary')
    #         # )
    #     )

class LoginForm(AuthenticationForm):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user','title', 'message','is_accomplished',)
    # user = forms.IntegerField(required=False, widget=forms.HiddenInput())


    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'user',
            'title',
            'message',
            'is_accomplished',

            ButtonHolder(
                Submit('post_edit', 'Done', css_class='btn-success')
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
