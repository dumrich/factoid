from django.db import models

class Article(models.Model):
    """Represent an Article"""
    title = models.CharField(max_length=200)
    #added_by
    description = models.CharField(max_length = 255)

    # Article Text
    article_text = models.TextField(blank=True, null=True)
    
    date_added = models.DateTimeField('Date Published')
    date_updated = models.DateTimeField('Date Updated')
    slug = models.SlugField(max_length=100, unique=True)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

class Source(models.Model):
    """Article Sources"""

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
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    date_added = models.DateTimeField('Date Published')
    author = models.CharField(max_length=255)

    url = models.URLField(max_length=500)

    org = models.CharField(max_length = 10, choices = NETWORKS, default = "other")
