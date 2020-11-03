from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=50, )
    paradigm = models.CharField(max_length=50)

    # show the title on admin page
    def __str__(self):
        return self.title
