from django.shortcuts import render
from User.forms import *
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,  redirect

# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'User/registrationform.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('order:home')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('order:home')
        return render(request, self.template_name, {'form': form})
