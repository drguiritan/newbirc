from wagtail.models import Page
from wagtail.models import Site
from home.models import SiteConfiguration
from home.models import SwiperMasterPage

def research_links(request):
  
    return {            
        
        "ure_page": Page.objects.filter(id=17).live().first(),
        "nhc_collection": Page.objects.filter(id=29).live().first(),
        "faculty_page": Page.objects.filter(id=34).live().first(),
        "collaboration_page": Page.objects.filter(id=36).live().first(),
        "publication_page": Page.objects.filter(id=37).live().first(),               
        "mv_page": Page.objects.filter(id=43).live().first(),
        "specify_page": Page.objects.filter(id=45).live().first(),
        "ipt_gbif_page": Page.objects.filter(id=46).live().first(),
        "photogrammetry_lab_page": Page.objects.filter(id=47).live().first(),
    }

def contact_link(request):
    return {
         "contact_page": Page.objects.filter(slug="contact-page").live().first(),
    }

def swiper_context(request):
    """
    Makes swiper_items available in all templates globally.
    """
    try:
        page = SwiperMasterPage.objects.first()
        swiper_items = page.swiper_items.all() if page else []
    except Exception:
        swiper_items = []
    
    return {
        'swiper_items': swiper_items
    }

def site_configuration(request):
    """
    Adds site-wide configuration to the template context
    """
    site = Site.find_for_request(request)
    home_url = site.root_page.url if site and site.root_page else "/"
    # Get the current site for this request
    
    if site:
        config = SiteConfiguration.for_site(site)
    else:
        config = None

    return {
        "home_url": home_url, 
        "site_config": config
    }
