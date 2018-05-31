from sqlrun.process_result import ProcessResult

class PyProcessor:

    def execute_process(self, generic_process):
        process_result = ProcessResult()
        generic_process.process_result = process_result

        try:
            exec(generic_process.command_text)
            process_result.set_end_time()
        except Exception as e:
            print("handled user python script exception", e)

    def __init__(self):
        pass
