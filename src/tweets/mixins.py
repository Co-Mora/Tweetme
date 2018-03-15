from django.forms.utils import ErrorList
from django import forms


class UserFormMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(UserFormMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must login to continue"])
            return self.form_invalid(form)


class UserOwner(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwner, self).form_valid(form)
        form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["The User not allowed to change anything."])

