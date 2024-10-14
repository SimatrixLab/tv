import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.url  # Return only the final URL
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    url = "http://10.99.99.99/player.php?stream=bk/4"
    fetched_url = fetch_url(url)

    # Save the fetched URL to a text file
    with open("fetched_url.txt", "w") as file:
        file.write(f"Fetched URL: {fetched_url}\n")

    print("Fetched URL saved to fetched_url.txt")
