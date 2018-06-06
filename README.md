# duckrun

- Utility to run a series of scripts and report the running times.  
- Initial support is for Redshift and Python.
- work in progress

## Redshift setup

- copy the config file and input your secrets.  An example config file can be found in the project root.

`cp redshift_config.yaml redshift_config.yaml`

- configure the yaml file with your settings
- execute the following using your config

`python redshift_run.py redshift_config.yaml`

## Python Demo

`make intagrationTest`

## Resdhift Sample Output

`$ python tests/integration_test/python_process_integration.py`

````
SUMMARY


start_time          end_time            processes      local_start_time    local_end_time
_______________________________________________________________________________________________
1528339130.748658   1528339131.1300669  2              06/06/18 22:38      06/06/18 22:38





DETAIL


step      process desc                            running_time (seconds)                  percent of total time
__________________________________________________________________________________________________________________________________
1         file1.sql                               0.1877                                  49.3
2         file2.sql                               0.1934                                  50.7


STD OUT


file1.sql
--------------------
1


file2.sql
--------------------
0.79304793653686

````


## Use Cases

- Testing the impact of databases changes on running time
- Automating a series of SQL Scripts

## Set Up

- add duckrun to your python path
- install depdendencies
    - `pip3 install -r ./requirements.txt`
 - configure YAML
    - `cp redshift_config_example.yaml redshift_config.yaml`


# Backlog

### report improvements

- csv output (or psv)

### post to S3

- post report results to S3

### Column headers to sql results

- sql results in stdout should show col headers
