from typing import List
import subprocess

class Executor:
    def execute(self, cmds: List[str]):
        proc = subprocess.run(cmds, capture_output=True)
        return CmdResult(proc.stdout.decode('utf-8'), proc.stderr.decode('utf-8'), proc.returncode)

class CmdResult:
    def __init__(self, stdout, stderr, returncode):
        self._stdout = stdout
        self._stderr = stderr
        self._returncode = returncode

    @property
    def stdout(self):
        return self._stdout
    @property
    def stderr(self):
        return self._stderr
    @property
    def returncode(self):
        return self._returncode

