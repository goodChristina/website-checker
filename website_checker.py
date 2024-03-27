import requests as r


def website_check(url):
    try:
        response = r.get(url)
        if response.status_code == 200:
            print(f"Website {url} is real: status code 200.")
        else:
            print(f"Website {url} returned status code {response.status_code}.")
    except r.ConnectionError:
        print(f"Website {url} could not be reached.")
    except r.exceptions.MissingSchema:
        print(f"Very bad URL {url}. You probably forget http:// or https://, right?")
    except Exception as e:
        print(f"This error occurred: {e}")



if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    website_check(url)
