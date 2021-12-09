from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


# Profile for a user.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    imageURL = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


class Animal(models.Model):
    name = models.CharField(max_length=255)

    taxPhylum = models.CharField(max_length=255)
    taxClass = models.CharField(max_length=255)
    taxOrder = models.CharField(max_length=255)
    taxFamily = models.CharField(max_length=255)
    taxGenus = models.CharField(max_length=255)
    taxSpecies = models.CharField(max_length=255)

    avgHeight = models.DecimalField()
    avgWidth = models.DecimalField()
    avgLength = models.DecimalField()
    avgWeight = models.DecimalField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('animal-detail', args=(str(self.id)))


class Sighting(models.Model):
    dateTime = models.DateTimeField()

    imageURL = models.TextField(blank=True, null=True)
    
    numberSeen = models.DecimalField()
    numberHeard = models.DecimalField()

    location = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    description = models.TextField()

    animal = models.ForeignKey(Animal,
                               on_delete=models.CASCADE,
                               )

    spotter = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='mySightings',
                                related_query_name="sighting"
                                )
    height = models.DecimalField()
    width = models.DecimalField()
    length = models.DecimalField()
    weight = models.DecimalField()
