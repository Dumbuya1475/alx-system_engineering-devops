import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Reddit API requires a User-Agent header

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # If subreddit is invalid or any other error
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit API: {e}")
        return 0

# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        if subscribers == 0:
            print("OK")
        else:
            print(subscribers)
