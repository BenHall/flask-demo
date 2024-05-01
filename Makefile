.PHONY: run test

run:
	@echo "Starting Flask application..."
	@python app.py

test:
	@echo "Running tests..."
	@python -m unittest discover -s tests

coverage:
	@coverage run -m unittest discover
	@coverage report
	@coverage html



install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

curl:
	@curl -d '{"name":"John", "age":30}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/postdata
