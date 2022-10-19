
from django.shortcuts import  get_object_or_404, render 
from blog.models import Article, Contact
from blog.forms import ContactForm, NouveauContactForm


# Create your views here.

#voici la vue lie a home



def home(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous selectionnons tous nos articles 
    return render(request, 'blog/add.html', {"all_articles": articles})



def read(request, id, slug):
    """ affiche l'article au complet """
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/tp1.html', {"article": article})


def contact(request):
    
    if request.method == 'POST': # s'il sagit d'une requete post
        form = ContactForm(request.POST) # nous reprenons les données
        
        if form.is_valid(): # nous vérifions les que les données envoyée sons valides
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            username = form.cleaned_data["username"]
            renvoi = form.cleaned_data["renvoi"]
            
            # nous pouvons ici envoyer l'email grace aux données que nous venos de recupérer
            
            envoi = True
        else: # si la methode n'est pas post 
            form = ContactForm() #nous creéons un formulaire vide
            
    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    saved = False
    
    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data["name"]
            contact.address = form.cleaned_data["address"]
            contact.email = form.cleaned_data["email"]
            contact.photo = form.cleaned_data["photo"]
        contact.save()
        saved = True
    else:
        form = NouveauContactForm()
    
    return render(request, 'blog/new_contact.html', locals())

def voir_contact(request):
    contacts = Contact.objects.all()
    return render(request,'list_contact.html',{'contacts':contacts})


def signup(request):
    render(request, 'blog/insrire.html')
        
            
            



