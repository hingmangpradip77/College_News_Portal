# In users/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login # <-- 1. IMPORT THE LOGIN FUNCTION

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # 2. CHANGE THE SUCCESS URL TO THE HOMEPAGE
    success_url = reverse_lazy('article_list') 
    template_name = 'registration/signup.html'

    # 3. ADD THIS METHOD TO LOG THE USER IN AUTOMATICALLY
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save() # Create the user
        login(self.request, user) # Log the user in
        return super().form_valid(form)