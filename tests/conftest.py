import pytest

@pytest.fixture(scope="session")
def browser_context_args():
    return {"timeout": 20000}  # Set default timeout to 15 seconds

# @pytest.fixture(scope="function")
# def context_options():
#     return {"record_video": {"dir": "videos/"}}