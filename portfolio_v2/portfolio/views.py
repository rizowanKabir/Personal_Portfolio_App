from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Service, Portfolio, Experience, Education
from .forms import ContactForm


def home(request):
    projects = Portfolio.objects.all()[:3]
    skills   = Skill.objects.all()[:12]
    services = Service.objects.all()[:3]
    return render(request, 'home.html', {
        'projects': projects,
        'skills':   skills,
        'services': services,
    })


def about(request):
    experiences = Experience.objects.all()
    educations  = Education.objects.all()
    return render(request, 'about.html', {
        'experiences': experiences,
        'educations':  educations,
    })


def skills(request):
    all_skills = Skill.objects.all()
    categories = {}
    for skill in all_skills:
        cat = skill.get_category_display()
        categories.setdefault(cat, []).append(skill)
    return render(request, 'skills.html', {'categories': categories})


def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services': all_services})


def portfolio(request):
    all_projects = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'projects': all_projects})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fix the errors below.')
    return render(request, 'contact.html', {'form': form})
