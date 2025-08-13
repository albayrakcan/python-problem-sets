import requests
import sys
import json


my_api_key = "987931f19078ad8b93f1afce38b1db58fc33ebc7e35a22b8c99fde3d8cd43dcc"


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + my_api_key
        )
        content = response.json()
    except requests.RequestException:
        sys.exit()

    print(f"${bitcoin*float(content["data"]["priceUsd"])}")


main()
