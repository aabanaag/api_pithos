from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class LeadDocument(Document):
    linkedin_url = fields.TextField(
        attr="linkedin_url",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    description = fields.TextField(
        attr="description",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    n_employee = fields.IntegerField(
        attr="n_employee",
        fields={"raw": fields.IntegerField()},
    )
    raw_json = fields.ObjectField(
        attr="raw_json",
        properties={
            "key": fields.TextField(),
            "value": fields.TextField(),
        },
    )
    company_name_linkedin = fields.TextField(
        attr="company_name_linkedin",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    url = fields.TextField(
        attr="url",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    urn = fields.TextField(
        attr="urn",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    campaign_id = fields.TextField(
        attr="campaign_id",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )

    class Index:
        name = "leads"

    class Django:
        model = "core.Lead"


@registry.register_document
class EmployeeDocument(Document):
    first_name = fields.TextField(
        attr="first_name",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    last_name = fields.TextField(
        attr="last_name",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    urn = fields.TextField(
        attr="urn",
        fields={"raw": fields.TextField(), "suggest": fields.CompletionField()},
    )
    raw_json = fields.ObjectField(
        attr="raw_json",
        properties={
            "key": fields.TextField(),
            "value": fields.TextField(),
        },
    )

    class Index:
        name = "employees"

    class Django:
        model = "core.Employee"
