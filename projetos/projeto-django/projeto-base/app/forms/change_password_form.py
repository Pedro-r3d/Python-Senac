from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class ChangePasswordForm(forms.Form):    
    current_password = forms.CharField(strip=False)
    new_password = forms.CharField(strip=False)
    confirm_new_password = forms.CharField(strip=False)
    
    class Meta:
        fields = [
            'current_password',
            'new_pasword',
            'confirm_new_pasword'
        ]
        
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get("current_password")
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if (
            self.user
            and current_password
            and not self.user.check_password(current_password)
        ):
            self.add_error("current_password", "A senha atual está incorreta.")

        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                self.add_error(
                    "confirm_new_password",
                    "As novas senhas não coincidem.",
                )
            else:
                try:
                    validate_password(new_password, self.user)
                except ValidationError as error:
                    self.add_error("new_password", error)

        return cleaned_data