import requests, secrets

def rotate_proxies():
    proxies = []
    with open("./proxies.txt", "r") as file:
        proxies = file.readlines()
        
    random_proxy = random_values(proxies)
    return f"http://{random_proxy.strip()}"
def random_values(d_lists):
    """
    Returns a random value from a list.

    Args
    """
    idx = secrets.randbelow(len(d_lists))
    return d_lists[idx]


res = requests.get(
    "https://www.google.com/",
    proxies = {
    'http': 'http://pbK6WTKK6aZInEMS:isp;us;@proxy.soax.com:9009',
    'https': 'http://pbK6WTKK6aZInEMS:isp;us;@proxy.soax.com:9009',
}

)

print(res.text)