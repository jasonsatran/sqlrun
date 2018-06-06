default: build

test:
	./test.sh	

integrationTest:
	python ./tests/integration_test/python_process_integration.py

runRedshift:
	python redshift_run.py redshift_config.yaml
