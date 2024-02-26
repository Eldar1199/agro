from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import DetailView


class ProductListView(View):
    template_name = 'infoproduct/list_category.html'

    def get(self, request, category_slug=None):
        categories = InfoCategory.objects.all()
        products_by_category = {}

        if category_slug:
            category = InfoCategory.objects.get(slug=category_slug)
            products_by_category[category] = Infoproduct.objects.filter(categories=category)

        context = {'categories': categories, 'products_by_category': products_by_category}
        return render(request, self.template_name, context)
    
class ProductDetailView(DetailView):
    model = Infoproduct
    template_name = 'infoproduct/product_detail.html'
    context_object_name = 'product'