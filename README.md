# sqlrun

Utility to run a series of Redshift scripts.

## Use Cases

- Testing the impact of databases changes on running time
- Automating a series of SQL Scripts

## Set Up

    pip3 install -r ./requirements.txt
    cp config_example.yaml config.yaml

# Backlog

## Redshift Processor

- execute_process() requires concrete implementation with setting of results

## Tests for Container

- container should loop through all processes

## Text Reporter

- requires an implementaiton.  it should take a list of process results and implement a report() function that formats a text table.
