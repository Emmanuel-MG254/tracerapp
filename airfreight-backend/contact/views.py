from django.http import Http404
from django.shortcuts import render
from .models import ContactMessage

def search_view(request):  # Example search view
    query = request.GET.get('q')
    # Assume searching for ContactMessage or other model
    results = ContactMessage.objects.filter(name__icontains=query)
    if not results.exists():
        raise Http404("No matching information found.")
    return render(request, 'contact/search_results.html', {'results': results})