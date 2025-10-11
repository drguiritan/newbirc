
from wagtail.models import Page

def downloadable_links(request):
  
    return {            
             
        "downloadable_page": Page.objects.filter(id=48).live().first(),
    }