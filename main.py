import aiohttp
import asyncio

async def fetch_url(url):
    try:
        # Asynchronously make a GET request with a 30-second timeout
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30) as response:
                response.raise_for_status()  # Check for HTTP errors
                return str(response.url)  # Return the final URL as a string
    except aiohttp.ClientError as e:
        return f"An error occurred: {e}"

async def main():
    url = "http://10.99.99.99/player.php?stream=bk/4"
    fetched_url = await fetch_url(url)

    # Save the fetched URL or error message to output.txt
    with open("output.txt", "w") as file:
        file.write(f"Fetched URL: {fetched_url}\n")

    print("Fetched URL saved to output.txt")

if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())
