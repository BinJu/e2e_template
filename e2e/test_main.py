from lib_proc import Executor

def test_cmd():
    executor = Executor()
    output = executor.execute(['docker', 'ps'])
    assert ":" in output.stdout

def test_pipe():
    executor = Executor()
    output = executor.pipe([["ls", "-l"], ["wc", "-l"]])
