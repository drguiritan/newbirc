from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.documents.models import Document
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from home.panels import PageIDPanel  

# =======================================================
# DownloadableFormsPage (Main Page)
# =======================================================
class DownloadableFormsPage(Page):
    """
    The main Wagtail page that serves as a hub for both:
    - Stand-alone downloadable files
    - Document groups (each with multiple subfiles)
    """

    intro = RichTextField(blank=True, help_text="Introductory text displayed above the groups/files.")

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        MultiFieldPanel(
            [
                InlinePanel('files', label="Standalone Files (not in any group)"),
            ],
            heading="Individual Documents"
        ),
        MultiFieldPanel(
            [
                InlinePanel('groups', label="Document Groups (with subfiles)",),
            ],
            heading="Grouped Documents",classname="collapsible"
        ),
    ]

    
    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]   

    class Meta:
        verbose_name = "Downloadable Forms Page"

    @classmethod
    def can_create_at(cls, parent):
        # Only allow creation if no other MissionVisionPage exists
        return super().can_create_at(parent) and not cls.objects.exists()
    
    def save(self, *args, **kwargs):
        # Ensure this is the only instance
        if not self.pk and DownloadableFormsPage.objects.exists():
            raise Exception("Only one Mission & Vision page can be created")
        super().save(*args, **kwargs)

    def get_context(self, request):
        """
        Adds 'groups' and 'files' to the page context for template rendering.
        """
        context = super().get_context(request)
        context['files'] = self.files.all()
        context['groups'] = self.groups.all()
        return context




# =======================================================
# DownloadableFile (Individual Document)
# =======================================================
# without sub files
class DownloadableFile(ClusterableModel):  
    """
    Represents a single, stand-alone downloadable file directly
    attached to the DownloadableFormsPage.
    Example: "Memorandum Form", "Research Proposal Template", etc.
    """

    page = ParentalKey(
        'DownloadableFormsPage',
        on_delete=models.CASCADE,
        related_name='files'
    )
    title = models.CharField(max_length=255, help_text="Title of the document.")
    description = models.TextField(blank=True, help_text="Optional short description of the document.")
    file = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='+',
        help_text="Upload the document file (PDF, DOCX, etc.)."
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('file'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Downloadable File"
        verbose_name_plural = "Downloadable Files"



# =======================================================
# DownloadableGroup (Group of Sub Files)
# =======================================================
class DownloadableGroup(ClusterableModel):
    """
    Represents a collection of subfiles under one category.
    Example: "Faculty Research Workshop" containing several downloadable forms.
    """

    page = ParentalKey(
        'DownloadableFormsPage',
        on_delete=models.CASCADE,
        related_name='groups'
    )
    group_image = models.ForeignKey(   
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Optional image representing this group (e.g., workshop photo)."
    )
    group_title = models.CharField(max_length=255, help_text="Name of this document group.")
    group_description = RichTextField(blank=True, help_text="Optional group overview or description.")

    panels = [
        FieldPanel('group_image'),
        FieldPanel('group_title'),
        FieldPanel('group_description'),
        InlinePanel('subfiles', label="Uploadable Files"),
    ]

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = "Downloadable Group"
        verbose_name_plural = "Downloadable Groups"



# =======================================================
# DownloadableSubFile (File within a Group)
# =======================================================
# with sub files
class DownloadableSubFile(ClusterableModel):
    """
    Represents a file that belongs to a specific group (DownloadableGroup).
    Example: "Ethics Approval Form" inside the "Faculty Research Workshop" group.
    """

    group = ParentalKey(
        'DownloadableGroup',
        on_delete=models.CASCADE,
        related_name='subfiles'
    )
    
    title = models.CharField(max_length=255, help_text="Title of the subfile document.")
    description = models.TextField(blank=True, help_text="Optional short description.")
    file = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='+',
        help_text="Upload the document file (PDF, DOCX, etc.)."
    )

    panels = [
        
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('file'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sub File"
        verbose_name_plural = "Sub Files"


#refers to notes_in_models.txt
