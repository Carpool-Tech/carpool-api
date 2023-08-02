from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    smoking = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    ranking = models.FloatField(default=0)
    rides_given = models.IntegerField(default=0)
    rides_taken = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="carpool_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="carpool_user_set",
        related_query_name="user",
    )


class Car(models.Model):
    FUEL_TYPES = [
        ("gasoline", "Gasoline"),
        ("electric", "Electric"),
        ("gas", "Gas"),
        ("ethanol", "Ethanol"),
        ("diesel", "Diesel"),
    ]

    owner = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    seats = models.IntegerField()
    plate = models.CharField(max_length=10)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    year = models.IntegerField()
    brand = models.CharField(max_length=50)
    last_maintenance = models.DateField(null=True, blank=True)


class Trip(models.Model):
    driver = models.ForeignKey(
        User, related_name="driven_trips", on_delete=models.CASCADE
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    actual_start_location = models.CharField(max_length=200)
    actual_end_location = models.CharField(max_length=200)
    actual_start_time = models.DateTimeField()
    actual_end_time = models.DateTimeField()
    actual_total_time = models.DurationField()
    total_carpool_tip = models.FloatField()
    is_finished = models.BooleanField(default=False)


class UserRoute(models.Model):
    user = models.ForeignKey(User, related_name="user_routes", on_delete=models.CASCADE)
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_divert_distance = models.FloatField(
        help_text="Maximum distance the user is willing to divert from the route, in km"
    )
