import os

import pytest


@pytest.fixture()
def hf_token() -> str:
    """
    Get the Hugging Face token from the environment variable HF_TOKEN_HUB_TESTS.

    If the variable is not set, the test using this fixture will be skipped.
    """
    token = os.environ.get("HF_TOKEN_HUB_TESTS")
    if not token:
        pytest.skip("HF_TOKEN_HUB_TESTS is not set")
    return token
