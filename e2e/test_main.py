from lib_proc import Executor

def test_abc():
    executor = Executor()
    output = executor.execute(['docker', 'ps'])
    assert ":" in output.stdout
