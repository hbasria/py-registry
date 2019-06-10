from registry import Registry
from tests.snake import Python, Anaconda


def test_register_manual_keys():
    registry = Registry()

    @registry.register(name='python')
    class PythonClass(Python):
        pass

    @registry.register(name='anaconda')
    class AnacondaClass(Anaconda):
        pass

    assert registry['python'] == PythonClass
    assert registry['anaconda'] == AnacondaClass
