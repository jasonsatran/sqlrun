import yaml
import os
import sys
from duckrun.container import Container
from duckrun.redshift.redshift_processor import RedshiftProcessor
from duckrun.generic_process_factory import GenericFileProcessFactory

def main():
    try:
        yaml = validate_input()
    except Exception as e:
        print("error loading configuration file, ", e)
        sys.exit(1)
    try:
        host = get_config_val(yaml, "host")
        sslmode = get_config_val(yaml, "sslmode")
        port = get_config_val(yaml, "port")
        user = get_config_val(yaml, "user")
        password = get_config_val(yaml, "password")
        database = get_config_val(yaml, "database")
        pathtosqlfiles = get_config_val(yaml, "pathtosqlfiles")
    except Exception as e:
        print("error reading configuration values, ", e)
        sys.exit(1)

    redshift_processor = processor = RedshiftProcessor(host, port, user, password, sslmode, database)
    sql_files = GenericFileProcessFactory.load_from_dir(pathtosqlfiles) 
    container = Container(redshift_processor, sql_files)
    container.run()

def validate_input():
    if len(sys.argv) != 2:
        raise Exception("exepcted exactly one input parameter")

    path_to_config = sys.argv[1]

    if not path_to_config:
        raise Exception("path to config must be 1st and only parameter")
    
    try:
        with open(path_to_config, "r") as f:
            yaml_obj = yaml.load(f)
    except:
        raise Exception("can not process expected yaml file: {}".format(path_to_config))

    return yaml_obj
    
def get_config_val(data, key):
    value = data.get(key)
    if value == None:
        errStr = "key not found: " + key
        raise Exception(errStr)
    return value

if __name__ == "__main__":
    main()
