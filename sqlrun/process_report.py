class ProcessReport:

    def __init__(self, processes):
        self._processes = processes

    def get_report(self):
        template = "{:10}{:40}{:20}"
        header = template.format("step","process desc", "running_time (seconds)")
        header_len = len(header)
        report_row = []
        report_row.append(header)
        report_row.append("-" * header_len)
        i = 1
        for process in self._processes:
            process_result = process.process_result
            print(type(process))
            print(type(process_result))
            print(process_result.running_time())
            if process_result == None:
                report_row.append(template.format(str(i), process.description, "No Result"))
            else:
                report_row.append(template.format(str(i), process.description, str(process_result.running_time())))
                
            i += 1
        return report_row

    def print(self):
        rpt = self.get_report()
        formatted_rpt = "\n".join(rpt)
        print(formatted_rpt)

