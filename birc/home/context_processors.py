from wagtail.models import Page,Site

def research_links(request):
    site = Site.find_for_request(request)
    home_url = site.root_page.url if site and site.root_page else "/"
    return {            
        "home_url": home_url, 
        "ure_page": Page.objects.filter(slug="ure-student-research").live().first(),
        # "faculty_page": Page.objects.filter(slug="faculty-research").live().first(),
        # "collaboration_page": Page.objects.filter(slug="collaboration-research").live().first(),
        # "publications_page": Page.objects.filter(slug="publications").live().first(),
    }
