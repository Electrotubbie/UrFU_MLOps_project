def pytest_addoption(parser):
    parser.addoption(
        "--dataset",
        default=[],
        type=str,
        action='append',
        help="path to dataset to test model",
    )

def pytest_generate_tests(metafunc):
    metafunc.parametrize("dataset", metafunc.config.getoption("dataset"))