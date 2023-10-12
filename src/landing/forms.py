from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from .models import CustomUser


class UserRegisterForm(forms.Form):

    input_class = "focus:outline-none p-2 lg:p-3 w-full rounded-md transition-colors placeholder:text-gray-300 lg:placeholder:text-gray-600 bg-transparent placeholder:font-title text-white lg:text-text font-medium lg:text-[18px] xl:text-[20px] xxl:text-[21px]"

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': input_class, 'placeholder': 'Email', 'required': False}),
    )

    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
                               'class': input_class, 'placeholder': 'Username'}),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': input_class, 'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={'class': input_class, 'placeholder': 'Confirm Password'}),
    )

    class Meta():
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required")

        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address")

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("This field is required.")
        if len(username) < 4:
            raise forms.ValidationError("At least 4 characters required.")

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError("This field is required.")
        if len(password1) < 6 or not any(char.isdigit() for char in password1):
            raise forms.ValidationError(
                "At least 6 characters and 1 number required.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("This field is required.")
        if len(password2) < 6 or not any(char.isdigit() for char in password2):
            raise forms.ValidationError(
                "At least 6 characters and 1 number required.")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class UserLoginForm(forms.Form):

    input_class = "focus:outline-none focus:border-accent border-2 border-transparent p-2 w-full bg-gray-100 transition-colors xl:p-3 xl:text- 19px"

    email_class = input_class + " mt-2 rounded-md"

    password_class = input_class + " rounded-l-md"

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': email_class, 'placeholder': 'Email', 'required': False}),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': password_class, 'placeholder': 'Password'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")

        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered.")

        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user is None:
                self.add_error('password', "Incorrect password.")

        return cleaned_data

    class Meta():
        model = CustomUser
        fields = ['email', 'password']


class CompleteRegisterForm(forms.ModelForm):

    avatar = forms.ImageField(
        label="Avatar",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'hidden', 'accept': 'image/*', 'id': 'file-input'}),

    )

    name = forms.CharField(

        label="Name",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'rounded-md w-full border-2 border-accent p-2 mt-3 focus:outline-none focus:border-primary text-[18px] md:text-[20px] font-title drop-shadow-md', 'placeholder': 'Enter your name', 'id': 'name'}),

    )

    bio = forms.CharField(

        label="Biography",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'resize-none rounded-md w-full border-2 border-accent p-2 mt-3 focus:outline-none focus:border-primary text-[18px] md:text-[20px] font-title drop-shadow-md', 'placeholder': 'Something about you...', 'rows': '5', 'id': 'bio'}),

    )

    class Meta:
        model = CustomUser
        fields = ('avatar', 'name', 'bio')