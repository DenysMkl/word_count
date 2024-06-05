IMAGE_NAME := counter-image

build:
	docker build -t ${IMAGE_NAME}:latest .

run: build
	docker compose up counter
