from django.shortcuts import render
from dish_search_app.models import Dish

# def search(request):
#     query = request.GET.get('query', '')  # Get the search query from the request

#     # Perform the search query on the Dish model
#     results = Dish.objects.filter(items__has_key=query).order_by('items__' + query)[:5]

#     context = {'query': query, 'results': results}
#     return render(request, 'search.html', context)

# def search(request):
#     query = request.GET.get('query', '')  # Get the search query from the request

#     # Perform the search query on the Dish model
#     results = Dish.objects.filter(items__has_key=query).order_by('items__' + query)[:5]

#     context = {'query': query, 'results': results}
#     return render(request, 'search.html', context)

# def search(request):
#     query = request.GET.get('query', '')  # Get the search query from the request

#     # Perform the search query on the Dish model
#     results = Dish.objects.filter(items__has_key=query).order_by('items__' + query)[:5]

#     context = {'query': query, 'results': results}
#     return render(request, 'search.html', context)

# from django.shortcuts import render
# from dish_search_app.models import Dish

def search(request):
    query = request.GET.get('query', '')  # Get the search query from the request

    # Perform the search query on the Dish model
    results = Dish.objects.filter(items__has_key=query).order_by('items__' + query)[:5]

    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)
