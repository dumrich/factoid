from django.db import models
from django.template.defaultfilters import slugify
from .createArticle import Media

CATEGORY_CHOICES = (
    ('technology', 'Technology'),
    ('science', 'Science'),
    ('politics', 'Politics'),
    ('health', 'Health'),
    ('arts', 'Arts'),
    ('sports', 'Sports'),
    ('business', 'Business'),
    ('world', 'World'),
    ('opinion', 'Opinion'),
)



class Article(models.Model):

    """Represent an Article"""
    author = models.CharField(max_length=200, blank=True, null=True)

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="thumbnails/")

    # Article Text
    article_text = models.TextField(blank=True, null=True)

    date_added = models.DateTimeField('Date Published',
                                      auto_now_add=True,
                                      blank=True)

    date_updated = models.DateTimeField('Date Updated',
                                        auto_now_add=True,
                                        blank=True)

    article_slug = models.SlugField(max_length=100,
                                    unique=True,
                                    blank=True,
                                    null=True)

    category = models.CharField(max_length=40,
                                blank=True,
                                null=True,
                                choices=CATEGORY_CHOICES)

    # Replace with One to Many

    def save(self, *args, **kwargs):
        self.article_slug = self.slug()

        sources = self.source_set.all()

        m = Media()
        for s in sources:
            m.addSource(s.source)

        # replace this with trained gpt-3 model
        self.article_text = m.gen_prompt()

        super().save(*args, **kwargs)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

class Source(models.Model):
    """Source Class"""
    CNN = "CNN"
    FOX = "FOX"
    NPR = "NPR"
    AP = "AP"
    MSNBC = "MSNBC"
    ABC = "ABC"
    CBS = "CBS"
    CNBC = "CNBC"
    NBC = "NBC"
    VICE = "VICE"
    BBC = "BBC"
    ESPN = "ESPN"

    NETWORKS = [
        (CNN, 'CNN'),
        (FOX, 'FOX'),
        (NPR, 'NPR'),
        (AP, 'AP'),
        (MSNBC, 'MSNBC'),
        (ABC, 'ABC'),
        (CBS, 'CBS'),
        (CNBC, 'CNBC'),
        (NBC, 'NBC'),
        (VICE, 'VICE'),
        (BBC, 'BBC'),
        (ESPN, 'ESPN'),
        ("other", "Other")
    ]

    source = models.URLField(max_length=300, blank=True, null=True)
    sourceOrg = models.CharField(
        max_length=10,
        choices=NETWORKS,
        default="other",
        blank=True,
        null=True)

    post = models.ForeignKey(Article, on_delete=models.CASCADE)
