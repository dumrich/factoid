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
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="thumbnails/")

    # Article Text
    article_text = models.TextField(blank=True, null=True)
    bibliography = models.TextField(blank=True, null=True)
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
    sourceOne = models.URLField(max_length=300, blank=True, null=True)

    sourceTwo = models.URLField(max_length=300, blank=True, null=True)

    sourceThree = models.URLField(max_length=300, blank=True, null=True)

    sourceFour = models.URLField(max_length=300, blank=True, null=True)

    sourceFive = models.URLField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.article_slug = self.slug()
        m = Media("Andrew Tate Detained in Romania",
                  "Bro got caught lackin in 4k")
        m.addSource(self.sourceOne)
        m.addSource(self.sourceTwo)
        m.addSource(self.sourceThree)
        m.addSource(self.sourceFour)
        m.addSource(self.sourceFive)
        # replace this with true machine learning
        self.article_text = m.gen_prompt()

        print(self.article_text)

        super().save(*args, **kwargs)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title
