from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class LeadDocument(Document):
    linkedin_url = fields.KeywordField()
    description = fields.TextField()
    n_employee = fields.IntegerField()
    raw_json = fields.ObjectField()
    company_name_linkedin = fields.KeywordField()
    url = fields.KeywordField()
    urn = fields.KeywordField()
    campaign_id = fields.KeywordField()

    class Index:
        name = "leads"

    class Django:
        model = "core.Lead"


@registry.register_document
class EmployeeDocument(Document):
    first_name = fields.KeywordField()
    last_name = fields.KeywordField()
    urn = fields.KeywordField()
    raw_json = fields.ObjectField()

    class Index:
        name = "employees"

    class Django:
        model = "core.Employee"
