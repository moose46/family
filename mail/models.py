import string
from datetime import date
# from importlib.resources._common import _

from django.db import models
from django.contrib.auth.models import User


# from django.utils.text import slugify
# from os import name


# Create your models here.
class Base(models.Model):
    createdAt = models.DateTimeField("date created", auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updatedAt = models.DateTimeField("date last updated", auto_now=True, null=True)

    class Meta:
        abstract = True


class Person(Base):
    name: str = models.CharField(max_length=32, default="", null=False, unique=True)
    slug: str = models.TextField(blank=True)

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None )
    #     self.slug = slugify(f"{self.name}")
    #     # print(self.slug)
    #     if update_fields is not None and name in update_fields:
    #         update_fields = {"slug"}.union(update_fields)
    #     super().save(
    #         force_insert=force_insert,
    #         force_update=force_update,
    #         using=using,
    #         update_fields=update_fields
    #     )

    def __str__(self) -> str:
        return self.name

    class META:
        unique_together = ["name", "role.name"]
        ordering = ["name"]
        unique = ["name"]


class State(Base):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return string.capwords(self.name)

    @property
    def state_name(self):
        return string.capwords(self.name)

    class META:
        unique = "name"
        ordering = "name"

class City(Base):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self) -> str:
        return self.name

class Address(Base):
    address_1 = models.CharField("address", max_length=128)
    address_2 = models.CharField("address cont'd", max_length=128, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip = models.CharField(max_length=32)
    # YOUR_STATE_CHOICES = list(STATE_CHOICES)
    # YOUR_STATE_CHOICES.insert(0, ('', '---------'))


    # city = models.CharField(_("city"), max_length=64, default="Zanesville")
    # state = USStateField(_("state"), default="OH")
    # zip_code = models.CharField(_("zip code"), max_length=5, default="43701",widget=forms.Select(
    #         choices=YOUR_STATE_CHOICES))


class MailFrom(Base):
    name: Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address: Address = models.ForeignKey(Address, on_delete=models.CASCADE)


class MailTo(Base):
    name: Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address: Address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Mail(Base):
    postmark: date = models.DateField()
    mail_to = models.ForeignKey(MailTo, on_delete=models.CASCADE)
    mail_from = models.ForeignKey(MailFrom, on_delete=models.CASCADE)
    contents = models.TextField()
