
get-dependencies:
	rm -rf $(HOME)/.m2/repository/* && \
	cd code-with-quarkus && \
	mvn quarkus:go-offline

list-dependencies:
	python3 parse_dependencies.py > dependencies.txt