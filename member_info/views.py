from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from member_info.forms import WhrsAuthenticatonForm

class WhrsLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = WhrsAuthenticatonForm

    def form_valid(self, form: WhrsAuthenticatonForm) -> HttpResponseRedirect:
        """Security check complete. Log the user in."""
        if form.user_require_password_reset():
            # redirect to the reset notification page and resend the reset email TODO
            return HttpResponseRedirect(self.get_success_url())
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
