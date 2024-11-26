from django.shortcuts import render, redirect
from .forms.ContactForm import ContactForm
from .forms.DevisForm import DevisForm
from django.contrib import messages


# Create your views here.


def index(request):
    callback = ''
    if request.method == 'POST':
        # date treatment
        form_devis = DevisForm(request.POST)
        if form_devis.is_valid():
            form_devis.save()
            messages.success(request, "Merci de nous avoir contacté, nous vous recontacterons bientot !")
            # callback = form_devis.date
            return redirect('home')
        else:
            print(f"Echec d'enregistrement du devis! {form_devis}")
    else:
        form_devis = DevisForm()
    context = {
        'form_devis': form_devis,
        'callback': callback
    }
    return render(request, "showcase_site/index.html", context)


def about(request):
    return render(request, "showcase_site/about.html")


def services(request):
    return render(request, "showcase_site/service.html")


def projects(request):
    return render(request, "showcase_site/project.html")


def team(request):
    return render(request, "showcase_site/team.html")


def testimonial(request):
    return render(request, "showcase_site/testimonial.html")


def blog_grid(request):
    return render(request, "showcase_site/blog.html")


def blog_detail(request):
    return render(request, "showcase_site/detail.html")


def contact(request):
    if request.method == 'POST':
        # date treatment
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci de nous avoir contacté, nous vous recontacterons bientôt !")
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, "showcase_site/contact.html", context)
