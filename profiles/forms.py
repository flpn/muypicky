from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered")
        
        return email

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError("Passwords don't match")

        return password_2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # Save the provided password in hashed format
        user.set_password(self.cleaned_data.get('password_1'))
        user.is_active = False

        if commit:
            user.save()
            user.profile.send_activation_email()
        
        return user