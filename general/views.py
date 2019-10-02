from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Proyecto,Categoria

# Create your views here.
class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = "list.html"

class CategoriaDetailView(generic.DetailView):
    model=Categoria
    template_name = "detail.html"

class CategoriaCreateView(generic.CreateView):
    model = Categoria
    fields='__all__'
    template_name = "form.html"


class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    fields='__all__'
    template_name = "form.html"


class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    template_name = "delete.html"
    success_url = reverse_lazy('tienda:index')

class ProyectoListView(generic.ListView):
    model = Proyecto
    template_name = "facturas-list.html"


class ProyectoDetailView(generic.DetailView):
    model = Proyecto
    template_name = "facturas-detail.html"

class ProyectoCreateView(generic.CreateView):
    model = Proyecto
    fields='__all__'
    template_name = "facturas-form.html"


class ProyectoUpdateView(generic.UpdateView):
    model = Proyecto
    fields='__all__'
    template_name = "facturas-form.html"


class ProyectoDeleteView(generic.DeleteView):
    model = Proyecto
    template_name = "facturas-delete.html"
    success_url = reverse_lazy('categoria:facturas-index')

   #def get_context_data(self, **kwargs):
    #    context = super(ProyectoDetailView, self).get_context_data(**kwargs)
     #   context["detalle"] = Detalle.objects.filter(factura=self.object)
      #  return context



# class DetalleInLine(InlineFormSetFactory):
  #  model = Detalle
   # fields = '__all__'

#class ProyectoCreateView(CreateWithInlinesView):
 #   model = Proyecto
  #  inlines = [DetalleInLine]
   # fields = '__all__'
   # template_name = "facturas-form.html"


#class ProyectoUpdateView(UpdateWithInlinesView):
 #   model = Proyecto
  #  inlines = [DetalleInLine]
   # fields = '__all__'
    #template_name = "facturas-form.html"


#class ProyectoDeleteView(generic.DeleteView):
 #   model = Proyecto
  #  template_name = "facturas-delete.html"
   # success_url = reverse_lazy('tienda:factura-index')