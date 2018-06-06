# duckrun

- Under Development.
- Utility to run a series of scripts and report the running times.  
- Initial support is planned for Redshift and Python.

## Sample Output

`$ python tests/integration_test/python_process_integration.py`

````
SUMMARY


start_time          end_time            processes      local_start_time    local_end_time
_______________________________________________________________________________________________
1528256959.273771   1528256959.2744598  2              06/05/18 23:49      06/05/18 23:49





DETAIL


step      process desc                            running_time (seconds)                  percent of total time
__________________________________________________________________________________________________________________________________
1         01_hello.py                             0.0001                                  8.3
2         02_exp.py                               0.0006                                  91.7


STD OUT


01_hello.py
--------------------
hello world



02_exp.py
--------------------
[No Standard Output]

````


## Use Cases

- Testing the impact of databases changes on running time
- Automating a series of SQL Scripts

## Set Up

### Redshift

    pip3 install -r ./requirements.txt
    cp redshift_config_example.yaml redshift_config.yaml

### Other Databases

- todo

# Backlog

### report improvements

- csv output (or psv)

### post to S3

- post report results to S3

### redshift

- extend for redshift usage

