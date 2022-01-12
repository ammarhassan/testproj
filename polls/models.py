from django.db import models


class Visits(models.Model):
	number = models.IntegerField(help_text='Number of visits', default=0, blank=True)