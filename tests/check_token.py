import os
import time

import requests

base = os.path.join("icons", "tokens")
sleep_time = 0.5

eth_address = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
sbtc_curve_address = "0xC25099792E9349C7DD09759744ea681C7de2cb66"
default_tokens = {
    eth_address: {
        "address": eth_address,
        "name": "Ethereum",
        "symbol": "ETH",
        "decimals": "18",
        "chainId": 1,
    },
    sbtc_curve_address: {
        "address": sbtc_curve_address,
        "name": "LP tBTC Curve",
        "symbol": "TBTCCURVE",
        "decimals": "18",
        "chainId": 1,
    },
}

ethplorer = os.environ.get("ETHPLORER_API_KEY")

required_files = ["logo.svg", "logo-32.png", "logo-128.png"]


def get_info(token):
    if token in default_tokens:
        return default_tokens[token]
    try:
        url = f"https://api.ethplorer.io/getTokenInfo/{token}?apiKey={ethplorer}"
        r = requests.get(url)
        return r.json()
    except:
        return None


def main():
    ok = True
    for token in os.listdir(base):
        root = os.path.join(base, token)
        for required in required_files:
            required = os.path.join(root, required)
            if not os.path.exists(required):
                print(f"Error: {required} does not exist but it's required.")
                ok = False
            if ethplorer:
                token_info = get_info(token)
                if token_info is None:
                    print(f"Error: {token} could not be fetched.")
                    ok = False
                time.sleep(sleep_time)
    if not ok:
        exit(1)


if __name__ == "__main__":
    main()
