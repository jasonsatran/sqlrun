from duckrun.generic_process import GenericProcess
import glob
import os

class GenericFileProcessFactory:

    @staticmethod
    def load_from_dir(root_dir):
        # path_with_sql = os.path.join(root_dir,"*.sql")
        # file_paths = glob.glob(path_with_sql)
        all_files = os.path.join(root_dir,"*")
        file_paths = glob.glob(all_files)
        file_paths.sort()
        processes = [GenericFileProcessFactory._create_process(y) for y in file_paths]
        return processes

    @staticmethod
    def _create_process(path_to_file):
        with open(path_to_file, "r") as f:
            command_text = f.read()
        base_name = os.path.basename(path_to_file)
        process = GenericProcess(command_text) 
        process.description = base_name
        return process
