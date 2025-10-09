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
 
    
ICON_CHOICES = [
    ("bi-calendar-check me-2", "Calendar Check"),
    ("bi-clock me-2", "Clock"),
    ("bi-binoculars me-2", "Binoculars"),
    ("bi-slash-circle me-2", "Slash Circle"),
    ("bi-geo-alt me-2", "Location"),
    ("bi-person me-2", "Person"),
]


class GenericFieldItem(models.Model):
    # site_config = models.OneToOneField(
    #     'SiteConfiguration',
    #     on_delete=models.CASCADE,
    #     related_name='generic_fields'
    # )

    site_config = ParentalKey(
        'SiteConfiguration',
        on_delete=models.CASCADE,
        related_name='generic_fields'
    )

    # Caption / Value / Icon
    
    caption1 = models.CharField(max_length=100, blank=True)
    value1 = models.CharField(max_length=100, blank=True)
    icon1 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    caption2 = models.CharField(max_length=100, blank=True)
    value2 = models.CharField(max_length=100, blank=True)
    icon2 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    caption3 = models.CharField(max_length=100, blank=True)
    value3 = models.CharField(max_length=100, blank=True)
    icon3 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    caption4 = models.CharField(max_length=100, blank=True)
    value4 = models.CharField(max_length=100, blank=True)
    icon4 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    caption5 = models.CharField(max_length=100, blank=True)
    value5 = models.CharField(max_length=100, blank=True)
    icon5 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    caption6 = models.CharField(max_length=100, blank=True)
    value6 = models.CharField(max_length=100, blank=True)
    icon6 = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True)

    panels = [
        FieldPanel("caption1"), FieldPanel("value1"), FieldPanel("icon1"),
        FieldPanel("caption2"), FieldPanel("value2"), FieldPanel("icon2"),
        FieldPanel("caption3"), FieldPanel("value3"), FieldPanel("icon3"),
        FieldPanel("caption4"), FieldPanel("value4"), FieldPanel("icon4"),
        FieldPanel("caption5"), FieldPanel("value5"), FieldPanel("icon5"),
        FieldPanel("caption6"), FieldPanel("value6"), FieldPanel("icon6"),
    ]

    def __str__(self):
        return self.caption1 or "Generic Item"

    class Meta:
        verbose_name = "Generic Item"
        verbose_name_plural = "Generic Items"

@register_setting
class SiteConfiguration(ClusterableModel,BaseSiteSetting):

    site_name = models.CharField(max_length=255, default="FSUU BIRC")
    phone_number = models.CharField(max_length=50, default="+91 123 654 7898")
    address = models.TextField(default="San. Francisco St. Butuan City, Philippines")
    email = models.EmailField(default="biodiversity@urios.edu.ph")
    developed_by = models.TextField(verbose_name="Developed By",default="© 2025 FSUU BIRC WEBSITE. All Rights Reserved | Developed by BIRC TEAM")
    footer_additional_info = models.TextField(verbose_name="A caption footer additional information for all site wide footer article page",blank=True,default="")
    fsuu_mv_caption = models.TextField(verbose_name="FSUU mision and vision caption",blank=True,default="Father Saturnino Urios University")
    birc_mv_caption = models.TextField(verbose_name="BIRC mision and vision caption",blank=True,default="Biodiversity Informatics Research Center")
    mv_ourteam_caption = models.TextField(verbose_name="Team Title",blank=True,default="Our Team")
    mv_ourteam_description = RichTextField(
        blank=True,
        features=[],  # Empty features list - no formatting allowed
        verbose_name="Team Short Description",
        help_text="Introduction text for this species",
        default="Meet the dedicated individuals behind our mission"
    )

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
                FieldPanel("footer_additional_info"),
                FieldPanel("developed_by"),            
            ],
            heading="Site wide configuration"
        ),
        MultiFieldPanel(
            [
                FieldPanel("fsuu_mv_caption"),
                FieldPanel("birc_mv_caption"),                
                FieldPanel("mv_ourteam_caption"),
                FieldPanel("mv_ourteam_description"), 
            ],
            heading="Mission and Vision Captions",classname="collapsed"
        ),
         InlinePanel("partners", label="BIRC Partner",classname="collapsed"), # Works because of ParentalKey
         InlinePanel("generic_fields", max_num=1, min_num=1, label="Generic MultiField Items",classname="collapsed"),         
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

    intro = RichTextField(
        blank=True,
        features=[],  # Empty features list - no formatting allowed
        help_text="Introduction text for this species"
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
        FieldPanel('intro'),     
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




class MissionVisionPage(Page):

    fsuu_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Father Saturnino Urios University Logo"
    )

    # FSUU Mission section
    fsuu_mission_title = models.CharField(max_length=255, default="FSUU Mission")
    fsuu_mission_content = RichTextField(features=['bold', 'italic', 'link'], blank=True)
    
    # FSUU Vision section  
    fsuu_vision_title = models.CharField(max_length=255, default="FSUU Vision")
    fsuu_vision_content = RichTextField(features=['bold', 'italic', 'link'], blank=True)
    
    # Page content
    fsuu_body = RichTextField(blank=True, features=['bold', 'italic', 'link', 'ol', 'ul'])


    birc_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Biodiversity Informatics Research Center Logo"
    )

    # BIRC Mission section
    birc_mission_title = models.CharField(max_length=255, default="Our Mission")
    birc_mission_content = RichTextField(features=['bold', 'italic', 'link'], blank=True)
    
    # Vision section  
    birc_vision_title = models.CharField(max_length=255, default="Our Vision")
    birc_vision_content = RichTextField(features=['bold', 'italic', 'link'], blank=True)
    
    # Page content
    birc_body = RichTextField(blank=True, features=['bold', 'italic', 'link', 'ol', 'ul'])
    
    

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('fsuu_logo', heading="Logo"),
                FieldPanel('fsuu_mission_title', heading="Mission Title"),
                FieldPanel('fsuu_mission_content', heading="Mission Content"),
                FieldPanel('fsuu_vision_title', heading="Vision Title"),
                FieldPanel('fsuu_vision_content', heading="Vision Content"),
                FieldPanel('fsuu_body', heading="Additional Content"),
            ],
            heading="FSUU Section",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('birc_logo', heading="Logo"),
                FieldPanel('birc_mission_title', heading="Mission Title"),
                FieldPanel('birc_mission_content', heading="Mission Content"),
                FieldPanel('birc_vision_title', heading="Vision Title"),
                FieldPanel('birc_vision_content', heading="Vision Content"),
                FieldPanel('birc_body', heading="Additional Content"),
            ],
            heading="BIRC Section",
            classname="collapsible collapsed"
        ),
        InlinePanel('personnel_items', label="Personnel"),
    ]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]   
    
    # Template
    template = "home/mv/mv_page.html"
    
    # Parent page type
    parent_page_types = ['home.HomePage']
    subpage_types = []
    
    class Meta:
        verbose_name = "Mission & Vision Page"
        verbose_name_plural = "Mission & Vision Pages"
    
    @classmethod
    def can_create_at(cls, parent):
        # Only allow creation if no other MissionVisionPage exists
        return super().can_create_at(parent) and not cls.objects.exists()
    
    def save(self, *args, **kwargs):
        # Ensure this is the only instance
        if not self.pk and MissionVisionPage.objects.exists():
            raise Exception("Only one Mission & Vision page can be created")
        super().save(*args, **kwargs)


class Personnel(ClusterableModel):
    page = ParentalKey(
        MissionVisionPage,
        on_delete=models.CASCADE,
        related_name='personnel_items'
    )
    
    name = models.CharField(max_length=255, help_text="Full name of the personnel")
    position = models.CharField(max_length=255, help_text="Job title or position")
    department = models.CharField(max_length=255, blank=True, help_text="Department or unit")
    email = models.EmailField(blank=True, help_text="Email address")
    phone = models.CharField(max_length=50, blank=True, help_text="Phone number")
    bio = RichTextField(
        features=['bold', 'italic', 'link', 'ol', 'ul'],
        blank=True,
        help_text="Short biography or description"
    )
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Profile photo"
    )
    order = models.IntegerField(default=0, help_text="Ordering number")
    
    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('department'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('photo'),
        FieldPanel('bio'),
        FieldPanel('order'),
    ]
    
    class Meta:
        verbose_name = "Personnel"
        verbose_name_plural = "Personnel"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"





#Start Swiper
class SwiperMasterPage(Page):

    content_panels = Page.content_panels + [ InlinePanel('swiper_items', label="Swiper Items",classname="collapsed"),]

    promote_panels = Page.promote_panels + [
        PageIDPanel(heading="Page ID")
    ]   
    
    # Template
    template = "home/swiper/swiper_page.html"
    
    # Parent page type
    parent_page_types = ['home.HomePage']
    subpage_types = []
    
    class Meta:
        verbose_name = "Swiper page"
        verbose_name_plural = "Swiper pages"
    
    @classmethod
    def can_create_at(cls, parent):
        # Only allow creation if no other MissionVisionPage exists
        return super().can_create_at(parent) and not cls.objects.exists()
    
    def save(self, *args, **kwargs):
        # Ensure this is the only instance
        if not self.pk and SwiperMasterPage.objects.exists():
            raise Exception("Only one swiper page can be created")
        super().save(*args, **kwargs)


    
class SwiperData(ClusterableModel):
    page = ParentalKey(
        SwiperMasterPage,
        on_delete=models.CASCADE,
        related_name='swiper_items'
    )
    
    name = models.CharField(max_length=795, help_text="Feature Name")
    alt_name = models.CharField(max_length=795,blank=True, help_text="Feature alternate name or intro")
    content = RichTextField(
        features=['bold', 'italic', 'link', 'ol', 'ul'],
        blank=True,
        help_text="Description"
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image for the feature"
    )

    pagelink = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Optional page link for this species information"
    )

    order = models.IntegerField(default=0, help_text="Ordering number")
    
    panels = [
        FieldPanel('name'),
        FieldPanel('alt_name'),
        FieldPanel('content'),
        FieldPanel('image'),
        PageChooserPanel('pagelink'),
        FieldPanel('order'),
    ]
    
    class Meta:
        verbose_name = "Swiper Data"
        verbose_name_plural = "Swiper Data"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    
#End Swiper