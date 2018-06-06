import time

class ProcessReport:

    def __init__(self, processes):
        self._processes = processes

    @staticmethod
    def format_second(sec):
	    return "{:.4f}".format(sec)

    @staticmethod
    def format_percent(x):
	    return "{:.1f}".format(x)

    def get_report(self):
        template = "{:10}{:40}{:40}{:40}"
        header = template.format("step","process desc", "running_time (seconds)", "percent of total time")
        header_len = len(header)
        report_row = []
        report_row.append(header)
        report_row.append("_" * header_len)
        i = 1
        for process in self._processes:
            process_result = process.process_result
            if process_result == None:
                report_row.append(template.format(str(i), process.description, "No Result"))
            else:
                report_row.append(template.format(str(i), 
                    process.description, 
                    ProcessReport.format_second(process_result.running_time),
                    ProcessReport.format_percent(process_result.percent_of_total())
                            )
                    )
            i += 1

        return report_row

    def standard_out(self):
        standard_out = []
        for process in self._processes:
            process_result = process.process_result
            standard_out.append(process.description)
            standard_out.append("--------------------")
            out = process.process_result.output
            if out.strip() == "":
                standard_out.append("[No Standard Output]")
            else:
                standard_out.append(str(out))
            standard_out.append('\n')

        return standard_out


    def get_report_header(self):
        header_row = []
        start_time  = self._processes[0].process_result.start_time
        end_time  = self._processes[-1].process_result.end_time
        processes_len = len(self._processes)
        template  = "{:20}{:20}{:15}{:20}{:20}"
        header = template.format("start_time", "end_time", "processes", "local_start_time", "local_end_time")
        header_len = len(header)
        header_data = template.format(str(start_time), str(end_time), str(processes_len), ProcessReport.local_time(start_time), ProcessReport.local_time(end_time))
        
        header_row.append(header)
        header_row.append("_" * header_len)
        header_row.append(header_data)
        header_row.append("\n\n")

        return "\n".join(header_row)
        
    @staticmethod
    def local_time(x):
        return str(time.strftime("%D %H:%M", time.localtime(int(x))))


    @staticmethod
    def print_section_title(title):

        print("\n")
        header =  title 
        print(header)
        print("\n")

    def print(self):

        ProcessReport.print_section_title("SUMMARY")
        report_header = self.get_report_header()
        print(report_header)
        
        rpt = self.get_report()
        ProcessReport.print_section_title("DETAIL")
        formatted_rpt = "\n".join(rpt)
        print(formatted_rpt)

        ProcessReport.print_section_title("STD OUT")
        std_out = self.standard_out()
        formatted_std_out = '\n'.join(std_out)
        print(formatted_std_out)



