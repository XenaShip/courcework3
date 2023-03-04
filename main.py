from utils import func


def main():
    OPERATION_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677769174003&signature=dSPXH_zkbz8InyyiumNfoTD1aPpC0kwflF-dJh9CWa4&downloadName=operations.json"
    LAST_OPERATIONS = 5
    FILTERED_EMPTY_FROM = True

    data, info = func.unpacking(OPERATION_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = func.get_filter(data, FILTERED_EMPTY_FROM)
    data = func.get_last(data, LAST_OPERATIONS)
    data = func.get_formatted_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
