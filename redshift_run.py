import os
from duckrun.generic_process import GenericProcess
from duckrun.generic_process_factory import GenericFileProcessFactory
from duckrun.redshift.redshift_processor import RedshiftProcessor
from duckrun.container import Container
from duckrun.process_report import ProcessReport
import yaml
import sys


def getConfigKey(key):
    value = data.get(key)
    if value == None:
        errStr = "key not found: " + key
        raise Exception(errStr)
    return value


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("exactly 1 argument is required which is the path to the yaml config")
        sys.exit(1)
    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("input path {0} does not exists".format(file_path))
        sys.exit(1)

    stream = open(sys.argv[1])  # path to yaml config is the first and only arg
    data = yaml.load(stream)
    host = getConfigKey("host")
    port = getConfigKey("port")
    user = getConfigKey("user")
    password = getConfigKey("password")
    sslmode = getConfigKey("sslmode")
    database = getConfigKey("database")
    pathtosqlfiles = getConfigKey("pathtosqlfiles")

    this_file_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_file_dir, pathtosqlfiles)
    abs_path = os.path.abspath(file_path)
    processes = GenericFileProcessFactory.load_from_dir(abs_path)
    processor = RedshiftProcessor(
        host, port, user, password, sslmode, database)
    container = Container(processor, processes)
    container.run()
    process_report = ProcessReport(processes)
    process_report.print()
