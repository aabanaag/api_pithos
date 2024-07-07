from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Lead(BaseModel):
    linkedin_url = models.URLField(max_length=200, unique=True)
    description = models.TextField()
    n_employee = models.IntegerField()
    raw_json = models.JSONField()
    company_name_linkedin = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    urn = models.CharField(max_length=200)
    campaign_id = models.CharField(max_length=200)

    def __str__(self):
        return self.campaign_id


class Employee(BaseModel):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    urn = models.CharField(max_length=200)
    raw_json = models.JSONField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
