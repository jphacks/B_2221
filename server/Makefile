init:
	python3 -m venv venv && \
	source ./venv/bin/activate && \
	pip install Flask matplotlib face_recognition

dev:
	flask --debug run

test:
	python -m unittest discover tests
