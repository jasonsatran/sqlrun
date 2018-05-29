# sqlrun

Utility to run a series of Redshift scripts.

## Use Cases

- Testing the impact of databases changes on running time
- Automating a series of SQL Scripts

## Set Up

    pip3 install -r ./requirements.txt
    cp config_example.yaml config.yaml

# Backlog

## Use yaml in main

- use yaml to read in configuration
    - include path to files

## Main implementation

## Tests for Container

- container should loop through all processes

## Text Reporter

- requires an implementaiton.  it should take a list of process results and implement a report() function that formats a text table.
