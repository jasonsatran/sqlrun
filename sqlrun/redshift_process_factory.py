from sqlrun.redshift_process import RedshiftProcess
import glob
import os

class RedshiftFileProcessFactory:

    @staticmethod
    def load_from_dir(root_dir):
        path_with_sql = os.path.join(root_dir,"*.sql")
        file_paths = glob.glob(path_with_sql)
        file_paths.sort()
        file_data = [RedshiftFileProcessFactory._get_file_data(x) for x in file_paths]
        processes = [RedshiftFileProcessFactory._create_process(y) for y in file_data]
        return processes

    @staticmethod
    def _get_file_data(path):
        with open(path, "r") as f:
            data = f.read()
        return data

    @staticmethod
    def _create_process(command_text):
        return RedshiftProcess(command_text)
