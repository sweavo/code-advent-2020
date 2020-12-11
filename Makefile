
test:
	python -m doctest *.py

coverage:
	coverage run --source=. -m doctest *.py
	coverage html
	@echo See htmlcov/index.html

profile:
	python -m cProfile day11_1.py
