from django_registration.forms import RegistrationForm
from django.contrib.auth import get_user_model
#from .models import User


class CustomUserForm(RegistrationForm):
    # TODO: add required fields to reg form

    class Meta(RegistrationForm.Meta):
        model = get_user_model()
        # TODO: specify all fields from Custom user model
        #  or make mew fields with define value or null