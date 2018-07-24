import uuid

from django.db import models


# Create your models here.
class TimeStampedCreateOnlyModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)


class TimeStampedModel(TimeStampedCreateOnlyModel):

    class Meta:
        abstract = True

    modified_at = models.DateTimeField(auto_now=True)


class Example(TimeStampedModel):

    class Meta:
        db_name = 'example_module_example'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
