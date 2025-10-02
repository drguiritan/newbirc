from wagtail.models import Page

def research_links(request):
    return {        
        "ure_page": Page.objects.filter(slug="ure-student-research").live().first(),
        # "faculty_page": Page.objects.filter(slug="faculty-research").live().first(),
        # "collaboration_page": Page.objects.filter(slug="collaboration-research").live().first(),
        # "publications_page": Page.objects.filter(slug="publications").live().first(),
    }
