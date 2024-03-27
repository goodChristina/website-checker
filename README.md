# Christina's Amazing Website Checker

This simple Python script checks if a website is valid for web scraping purposes. Skip the hassle of going to Google, entering the website URL and then clicking on it to see if it exists. This uses the `requests` library for HTTP requests to the entered URL and checks if for status code 200 (VALID), which shows that the website is accessible all from the ease of your source-code editor of choice!

## Features

- Validates website accessibility for web scraping
- Alerts the user if the website is not reachable with a non-200 status code
- Supports both HTTP and HTTPS URLs (wow!)

## How to Use

1. Make sure you have Python installed on your system. If not, you can download and install it from the official Python website: [Python.org](https://www.python.org/). Make sure it's the new version (3.something). Most Macbooks come with the 2 version, so check that the 3 version hasn't been accidentally uninstalled if the *print(f"blah-blah {var}")* doesn't work. 

2. Install the `requests` library using pip:

    ```
    pip install requests
    ```

3. Clone or download the repository to your local machine.

4. Open a terminal or command prompt and navigate to the directory containing the script (`website_checker.py`).

5. Run the script by executing the following command:

    ```
    python3 website_checker.py
    ```

6. Enter the URL of the website you want to check when prompted.

7. The script will output whether the website is valid for web scraping or not based on the HTTP response status code.ry

8. If none of these options work, you can try:
   
    ```
   import requests as r
   url = "https://....."
   site = r.get(url)
   print(site)
    ```
It does the exact same thing. 

## Contributing

Contributions are welcome, but it's hard to beat perfection!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

