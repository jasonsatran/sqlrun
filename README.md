# sqlrun

Utility to run a series of Redshift scripts.

## Use Cases

- Testing the impact of databases changes on running time
- Automating a series of SQL Scripts

## Set Up

### Redshift

    pip3 install -r ./requirements.txt
    cp recshift_config_example.yaml redshift_config.yaml

### Other Databases

- todo

# Backlog

## Main implementation

- implemented but needs to be tested

## Create Reports

- loop through all processes and create a table of process results

- requires an implementaiton.  it should take a list of process results and implement a report() function that formats a text table.
