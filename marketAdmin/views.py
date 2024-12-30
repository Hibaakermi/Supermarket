from itertools import chain
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import vegitables,grocrey,Product,ContactMessage
from django.db.models import Q
from .forms import ContactForm



class VegitableList(ListView):
  
    model = vegitables
    
    template_name = 'marketAdmin/vegitables.html'
    context_object_name = 'grocery'
    ordering = ['id']
    paginate_by = 7



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context
  
class GroceryList(ListView):
    model = grocrey
    template_name = 'marketAdmin/groce.html'
    context_object_name = 'vegitables'
    ordering = ['id']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context
  

class SearchView(ListView):
    template_name = 'marketAdmin/search_results.html'  # Template pour afficher les résultats
    context_object_name = 'results'  # Nom de la variable pour les résultats
    paginate_by = 7  # Nombre d'éléments par page

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()  # Récupérer la requête de recherche
        if query:
            # Recherche dans le modèle vegitables
            veg_results = vegitables.objects.filter(
                Q(vname__icontains=query)  # Recherche par le nom des légumes
            )
            # Recherche dans le modèle grocrey
            grocery_results = grocrey.objects.filter(
                Q(gname__icontains=query)  # Recherche par le nom des produits d'épicerie
            )
            # Recherche dans le modèle Product (si vous avez un modèle de produits distinct)
            product_results = Product.objects.filter(
                Q(name__icontains=query)  # Recherche par nom de produit
            )

            # Combiner les QuerySets
            combined_results = chain(veg_results, grocery_results, product_results)
            return sorted(combined_results, key=lambda x: x.id)  # Trier par ID pour un ordre stable

        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '').strip()  # Ajouter la requête au contexte
        context['userdata'] = self.request.userdata  # Ajouter userdata si nécessaire
        return context
    
def contact_us(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact_message = ContactMessage(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message']
        )
        contact_message.save()

        # Affiche un message de succès
        return render(request, 'marketAdmin/contact_us.html', {'form': form, 'success': True})
    return render(request, 'marketAdmin/contact_us.html', {'form': form, 'success': False})