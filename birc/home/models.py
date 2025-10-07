from django.db import models
from wagtail.models import Page,Orderable
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel,MultiFieldPanel,PageChooserPanel,InlinePanel
from wagtail.images.models import Image
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock, CharBlock,  PageChooserBlock,URLBlock

from .field_panels import FileUploadPanel
from .forms import SpeciesDataTableForm
from .panels import ReadOnlyTablePanel,PageIDPanel  


#The Master Page
class HomePage(Page):
    class Meta:
        verbose_name = "BIRC CONTENT MENU"



# URE Master Page
class StudentResearchPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        
    ]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]
    
    subpage_types = ["ResearchArticlePage"]

    class Meta:
        verbose_name = "Creating pages for URE only"


# URE Child Page
class ResearchArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Thumbnail image for listings"
    )

    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g. Adviser, Year, Category

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("thumbnail_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["StudentResearchPage"]
    subpage_types = []


# Faculty Master Page
class FacultyResearchPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        
    ]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]
    
    subpage_types = ["FacultyArticlePage"]

    class Meta:
        verbose_name = "Creating pages for Faculty Research only"


# Faculty Research Child Page
class FacultyArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Thumbnail image for listings"
    )

    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g. Adviser, Year, Category

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("thumbnail_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["FacultyResearchPage"]
    subpage_types = []



# Collaboration Master Page
class CollaborationResearchPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        
    ]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]
    
    subpage_types = ["CollaborationArticlePage"]

    class Meta:
        verbose_name = "Creating pages for Collaboration Research only"


# Collaboration Research Child Page
class CollaborationArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Thumbnail image for listings"
    )

    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g. Adviser, Year, Category

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("thumbnail_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["CollaborationResearchPage"]
    subpage_types = []


# Publication Master Page
class PublicationResearchPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        
    ]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]
    
    subpage_types = ["PublicationArticlePage"]

    class Meta:
        verbose_name = "Creating pages for Publication Research only"


# Publication Research Child Page
class PublicationArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Thumbnail image for listings"
    )

    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g. Adviser, Year, Category

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("thumbnail_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["PublicationResearchPage"]
    subpage_types = []

#site wide Master Page
class SiteWidePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="preferred size 190x214"
    )
    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)  # main content for the page

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
    ]

    subpage_types = ['SiteWideArticlePage']  # No child pages allowed, or list allowed page types

    class Meta:
        verbose_name = "Creating pages for other purpose"

#site wide Child Pages
class SiteWideArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g., Author, Category, Date

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["SiteWidePage"]  # can only be added under SiteWidePage
    subpage_types = []  # cannot have child pages

    class Meta:
        verbose_name = "Site-wide Article Page"




# Partner model linked to SiteConfiguration
class Partner(models.Model):
    site_config = ParentalKey(   #the parental
        'home.SiteConfiguration', # Link to the settings model
        on_delete=models.CASCADE,
        related_name='partners'
    )
    title = models.CharField(max_length=255, blank=True)
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    logo = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel("title"),
        PageChooserPanel("page"),
        FieldPanel("logo"),
    ]

    def __str__(self):
        return self.title or "Partner"
 
    

@register_setting
class SiteConfiguration(ClusterableModel,BaseSiteSetting):

    site_name = models.CharField(max_length=255, default="FSUU BIRC")
    phone_number = models.CharField(max_length=50, default="+91 123 654 7898")
    address = models.TextField(default="San. Francisco St. Butuan City, Philippines")
    email = models.EmailField(default="biodiversity@urios.edu.ph")

    site_description = RichTextField(
        blank=True,
        verbose_name="About the site",
        default="",
        features=['bold', 'italic', 'link', 'image', 'h2', 'h3', 'ol', 'ul'],  # Enable images
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                FieldPanel("phone_number"),
                FieldPanel("address"),
                FieldPanel("email"),
                FieldPanel("site_description"),
            
            ],
            heading="Site wide configuration"
        ),
         InlinePanel("partners", label="BIRC Partner"), # Works because of ParentalKey
    ]

    class Meta:
        verbose_name = "Site Configuration"




#for NHC Species Collection
# for Natural History Collection Species Data Table
# Species Collection
class CollectionPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
    ]


    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]

    subpage_types = ["SpeciesDataTable"]

    class Meta:
        verbose_name = "Creating pages for Natural History Collection only"




# Define the gallery model FIRST
class SpeciesGalleryImage(Orderable):
    """
    Gallery image for species data table.
    """
    page = ParentalKey(
        'SpeciesDataTable',  # Use string reference since SpeciesDataTable is defined below
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional caption for the species image"
    )

    pagelink = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Optional page link for this species information"
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
        PageChooserPanel('pagelink'),
    ]

    class Meta:
        verbose_name = "Species Image"
        verbose_name_plural = "Species Images"

class SpeciesDataTable(Page):
    """
    Page model for storing and displaying species data in tabular format.
    """
    description = RichTextField(
        blank=True,
        help_text="Description of this species collection",
        features=['bold', 'italic', 'link', 'ol', 'ul', 'h2', 'h3', 'h4', 'image']
    )

    columns = models.JSONField(
        blank=True, 
        null=True, 
        verbose_name="Column Names",
        help_text="Array of column names for the table"
    )
    
    base_form_class = SpeciesDataTableForm

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Gallery Images"),
        MultiFieldPanel([
            FileUploadPanel('columns_file'),
            FileUploadPanel('rows_file'),
        ], heading="Import Species Dataset Files", classname="collapsed"),
        ReadOnlyTablePanel('rows', 'columns', 'Species Data Table'),
    ]

    parent_page_types = ["CollectionPage"]
    subpage_types = []

    class Meta:
        verbose_name = "Species Data Table"
        verbose_name_plural = "Species Data Tables"

    def get_row_count(self):
        """Helper method to get the number of rows."""
        return self.rows.count()

    def get_column_count(self):
        """Helper method to get the number of columns."""
        return len(self.columns) if self.columns else 0
    

class SpeciesDataRow(models.Model):
    """
    Model for storing individual rows of species data.
    """
    page = ParentalKey(
        SpeciesDataTable, 
        related_name='rows', 
        on_delete=models.CASCADE
    )
    cells = models.JSONField(
        blank=True, 
        null=True,
        help_text="Array of cell values for this row"
    )
    
    panels = []

    class Meta:
        verbose_name = "Species Data Row"
        verbose_name_plural = "Species Data Rows"
        ordering = ['id']
        indexes = [
            models.Index(fields=['page', 'id']),  # For faster row lookups
        ]

    def __str__(self):
        return f"Row {self.pk} for {self.page.title}"    
    

#for Species profile only

class SepciesPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
    ]


    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]

    subpage_types = ["SpeciesProfilePage"]

    class Meta:
        verbose_name = "Creating pages for Species Profile Only"    

class SpeciesProfilePage(Page):
    """
    Detailed page for a single species.
    """
        
    body = StreamField([
        ('heading_h1', blocks.CharBlock(classname="full title", label="Heading H1")),
        ('heading_h2', blocks.CharBlock(classname="full title", label="Heading H2")),
        ('heading_h3', blocks.CharBlock(classname="full title", label="Heading H3")),
        ('paragraph', RichTextBlock(label="Paragraph")),
        ('image', ImageChooserBlock(label="Image")),
        ('quote', CharBlock(label="Quote", classname="quote-block", help_text="Short quote")),        
        ('page_link', PageChooserBlock(label="Page Link")),  # Links to another Wagtail page
        ('external_url', URLBlock(label="External URL", help_text="external link")),
    ], blank=True, use_json_field=True)  # Wagtail 7 uses JSONField by default
    
    content_panels = Page.content_panels + [        
        FieldPanel('body'),
    ]

    parent_page_types = ['SepciesPage']
    subpage_types = []
    
    class Meta:
        verbose_name = "Species Profile"   
        verbose_name_plural = "Species Profiles"     