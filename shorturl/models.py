import string
import random
from django.db import models

def generate_short_code():
    """Generate a random 6-character code for the short URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
