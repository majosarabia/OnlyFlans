from django.db import models
import uuid


class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    precio = models.DecimalField(decimal_places=0, max_digits=6, default=10000)

    def __str__(self):
        return f"{self.name} - ({self.flan_uuid}) - ¿Es Privado?: {self.is_private}"


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    customer_email = models.EmailField()
    customer_name = models.CharField()
    message = models.TextField()


class Tag(models.Model):
    tag_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    flans = models.ManyToManyField(Flan, related_name="tags")

    def __str__(self):
        return f"{self.name} - ({self.tag_uuid})"
