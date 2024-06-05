IMAGE_NAME := counter-image
VENV := venv

build:
	docker build -t ${IMAGE_NAME}:latest .

run: build
	docker compose up counter

create-venv:
	python3 -m venv ${VENV}
	@echo "Activate venv by writing: source ${VENV}/bin/activate"
