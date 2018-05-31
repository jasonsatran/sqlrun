from sqlrun.redshift.redshift_process import RedshiftProcess
import glob
import os

class RedshiftFileProcessFactory:

    @staticmethod
    def load_from_dir(root_dir):
        path_with_sql = os.path.join(root_dir,"*.sql")
        file_paths = glob.glob(path_with_sql)
        file_paths.sort()
        processes = [RedshiftFileProcessFactory._create_process(y) for y in file_paths]
        return processes

    @staticmethod
    def _create_process(path_to_file):
        with open(path_to_file, "r") as f:
            command_text = f.read()
        base_name = os.path.basename(path_to_file)
        process = RedshiftProcess(command_text) 
        process.description = base_name
        return process
