import yaml
import os
import sys
from sqlrun.container import Container
from sqlrun.redshift_processor import RedshiftProcessor
from sqlrun.redshift_process_factory import RedshiftFileProcessFactory

def main():
    try:
        yaml = validate_input()
    except Exception as e:
        print("error loading configuration file, ", e)
        sys.exit(1)

    print(yaml)
    try:
        port = get_config_val(yaml, "port")
        user = get_config_val(yaml, "user")
        password = get_config_val(yaml, "password")
        database = get_config_val(yaml, "database")
        path_to_files = get_config_val(yaml, "path_to_files")
    except Exception as e:
        print("error reading configuration values, ", e)
        sys.exit(1)

    print("in main")


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
