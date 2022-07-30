from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Category, Company, Feeback
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib import messages


# Create your views here.
def home(request):
    companies = Company.objects.all()
    context = {'companies':companies}
    return render(request, 'index.html', context)


def dashboard(request):
    companies = Company.objects.filter(user=request.user)

    context = {
        'companies':companies
    }
    return render (request, 'dashboard.html', context)


def viewCompany(request, slug):
    company = get_object_or_404(Company, slug=slug)
    return render(request, 'viewCompany.html', {
        'company':company
    })

def viewForNonUser(request, slug):
    company = get_object_or_404(Company, slug=slug)
    return render(request, 'views.html', {'company':company})

class Edition(UpdateView):
    model = Company
    fields = ['category', 'company_name', 'logo', 'company_website', 'company_email', 'twitter', 'linkedln',
    'headquarters',  'area_served', 'founders', 'founded', 'net_worth', 'revenue', 
    'taxpayer_identification_number', 'about',]
    template_name = 'edition.html'
    success_url = reverse_lazy('Dashboard')

class AddCompany(CreateView):
    model = Company
    fields = ['category', 'company_name', 'logo', 'company_website', 'company_email', 'twitter', 'linkedln',
    'headquarters',  'area_served', 'founders', 'founded', 'net_worth', 'revenue', 
    'taxpayer_identification_number', 'about',]
    template_name = 'AddCompany.html'
    success_url = reverse_lazy('Dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (AddCompany, self).form_valid(form)

class Feedback(CreateView):
    model = Feeback
    fields = ['name', 'email', 'message', ]
    template_name = 'feedback.html'
    success_url = reverse_lazy('Dashboard')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email or user name Already taking')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('Dashboard')
        else:
            messages.info(request, 'Password Not Match')
            return redirect('register')   
        return redirect ('/')     
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Dashboard')
        else:
            messages.info(request, 'Invalid Credential') 
            return redirect('login')
    else:        
        return render(request, 'login.html')