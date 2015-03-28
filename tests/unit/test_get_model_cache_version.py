import pytest
import mock

from cache_version.models import get_model_cache_version

def describe_get_model_cache_version():
    @pytest.fixture
    def model():
        return mock.sentinel.MODEL

    @pytest.fixture
    def mocked_inspect_model(mocker):
        return mocker.patch('cache_version.models.InspectModel')

    @pytest.fixture
    def mocked_hashlib(mocker):
        return mocker.patch('cache_version.models.hashlib')

    def it_should_inspect_the_target_model(model, mocked_inspect_model):
        get_model_cache_version(model)

        mocked_inspect_model.assert_called_once_with(model)

    def it_should_return_a_hash_of_all_field_names_and_field_types(model, mocked_inspect_model, mocked_hashlib):
        get_model_cache_version(model)

        mocked_hashlib.sha1(mock.ANY).hexdigest.assert_called_once_with()
