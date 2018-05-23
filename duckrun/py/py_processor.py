from duckrun.process_result import ProcessResult
import sys
from io import StringIO
import contextlib

# source:  https://stackoverflow.com/questions/3906232
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class PyProcessor:

    def execute_process(self, generic_process):
        process_result = ProcessResult()
        generic_process.process_result = process_result

        with stdoutIO() as s:
            try:
                exec(generic_process.command_text)
                process_result.set_end_time()
                process_result.output = s.getvalue()
            except Exception as e:
                print("handled user python script exception", e)
        return process_result

    def __init__(self):
        pass
