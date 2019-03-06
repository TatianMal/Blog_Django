from django_registration.forms import RegistrationForm

from .models import User


class CustomUserForm(RegistrationForm):
    # TODO: add required fields to reg form

    class Meta(RegistrationForm.Meta):
        model = User
        # TODO: specify all fields from Custom user model
        #  or make mew fields with define value or null