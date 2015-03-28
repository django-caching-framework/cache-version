import hashlib
from inspect_model import InspectModel

def get_model_cache_version(model):
    inspected_model = InspectModel(model)

    fields_and_types = {}

    for field in inspected_model.fields:
        fields_and_types[field] = getattr(model, field)

    for field in inspected_model.relation_fields:
        fields_and_types[field] = getattr(model, field)


    for field in inspected_model.many_fields:
        fields_and_types[field] = getattr(model, field)

    return hashlib.sha1(str(fields_and_types).encode('utf-8')).hexdigest()
