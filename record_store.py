record_store = {
    "records": [
        {
            "record_name": "Revolver",
            "artist": "The Beatles",
            "year_released": "1968",
            "in_stock": True,
            "number_in_stock": 2,
        },
        {
            "record_name": "The Wall",
            "artist": "Pink Floyd",
            "year_released": "1979",
            "in_stock": True,
            "number_in_stock": 1,
        },
        {
            "record_name": "LA Woman",
            "artist": "The Doors",
            "year_released": "1971",
            "in_stock": False,
            "number_in_stock": 0,
        },
        {
            "record_name": "After The Gold Rush",
            "artist": "Neil Young",
            "year_released": "1970",
            "in_stock": True,
            "number_in_stock": 3,
        },
        {
            "record_name": "Abbey Road",
            "artist": "The Beatles",
            "year_released": "1969",
            "in_stock": True,
            "number_in_stock": 2,
        },
        {
            "record_name": "The Rise and Fall of Ziggy Stardust and the Spiders From Mars",
            "artist": "David Bowie",
            "year_released": "1972",
            "in_stock": True,
            "number_in_stock": 2,
        },
        {
            "record_name": "IV",
            "artist": "Led Zepplin",
            "year_released": "1971",
            "in_stock": False,
            "number_in_stock": 0,
        },
    ]
}
# Create a function to get the number of records in stock
def get_records_store_stock_number(record_store):
    current_stock = 0
    for record in record_store["records"]:
        current_stock += record["number_in_stock"]
    print(f"We currently have {current_stock} records in stock")


get_records_store_stock_number(record_store)
print("-------------------------------------------")

# Return a list of all the artists in the record store
def get_list_of_artists(record_store):
    artist_list = []
    for record in record_store["records"]:
        artist_list.append(record["artist"])
    return artist_list


print(get_list_of_artists(record_store))
print("-------------------------------------------")

# Find out if a record is in stock by name
def find_if_record_in_stock(record_store, record_name):
    for record in record_store["records"]:
        if record_name == record["record_name"]:
            print(f"{record_name} is in stock")


find_if_record_in_stock(
    record_store, "The Rise and Fall of Ziggy Stardust and the Spiders From Mars"
)
