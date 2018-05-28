from sqlrun.redshift_process import RedshiftProcess
from os import listdir

class RedshiftFileProcessFactory:

    @staticmethod
    def load_from_dir(root_dir, self):
        file_paths = listdir(root_dir).sorted
        file_data = map(RedshiftFileProcessFactory._get_file_data, file_paths)
        processes = map(RedshiftFileProcessFactory._create_process, file_data)
        return processes

    @staticmethod
    def _get_file_data(path):
        with open(path, "r") as f:
            data = f.readlines()
        return data

    @staticmethod
    def _create_process(command_text):
        return RedshiftProcess(command_text)
