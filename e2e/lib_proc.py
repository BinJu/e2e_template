from typing import List
import subprocess

class Executor:
    def execute(self, cmds: List[str]):
        proc = subprocess.run(cmds, capture_output=True)
        return CmdResult(proc.stdout.decode('utf-8'), proc.stderr.decode('utf-8'), proc.returncode)
    def pipe(self, pipe_cmds: List[List[str]]):
        last_process = None
        final_cmds = pipe_cmds.pop()
        for cmds in pipe_cmds:
            if last_process is None:
                stdin = None
            else:
                stdin = last_process.stdout

            cur_process = subprocess.Popen(cmds, stdin=stdin, stdout=subprocess.PIPE)
            last_process = cur_process
        proc = subprocess.run(final_cmds, stdin=last_process.stdout, capture_output=True)
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

