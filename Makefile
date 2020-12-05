coverage:
	coverage run --source=. -m doctest *.py
	coverage html
	@echo See htmlcov/index.html

profile:
	python -m cProfile day5_2.py
