.PHONY: test health tools snapshot run

test:
	python -m pytest tests/ -q

health:
	python bin/uj health

tools:
	python bin/uj tools

snapshot:
	python bin/uj snapshot

run:
	python bin/uj run --all
