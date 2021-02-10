import pytest
from model_bakery import baker

@pytest.fixture()
def image_factory():
    def factory(**kwargs):
        images = baker.make("imgresize.Img", **kwargs)
        return images
    return factory