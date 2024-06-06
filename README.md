# Word Counter

### Prerequisites
1. Python 3.9+
2. Docker

### Clone repository
```
git clone https://github.com/DenysMkl/word_count.git
```

### Setup workplace
1. Install virtual environment (not required)
   * On Linux/MacOS
     ```
     make create-venv
     ```
   * On Windows
     ```
     python -m venv venv
     ```
2. Activate virtual environment
   * On Linux/MacOS
     ```
     source venv/bin/activate
     ```
   * On Windows
     ```
     venv\Scripts\activate
     ```
3. Install the dependencies
   * On Linux/MacOS
     ```
     make dev
     ```
   * On Windows
     ```
     pip install -r requirements.txt
     ```
4. Run
   * On Linux/MacOS
       ```
       python3 src/counter.py
       ```
    * On Windows
       ```
       cd src
       python src/counter.py
       ```
5. Run tests
   * On Linux/MacOS/Windows
     ```
     pytest --cov=. -v
     ```
6. Docker usage
    * Build the image
        ```
        make build
        ```
    * Run Docker container
        ```
        make run
        ```
