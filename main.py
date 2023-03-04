
from utils import func


def main():
    FILENAME = 'utils/operations.json'
    LAST_OPERATIONS = 5
    FILTERED_EMPTY_FROM = True

    data, info = func.unpacking(FILENAME)
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
