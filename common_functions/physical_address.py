import usaddress
from scourgify import normalize_address_record

def standardize_address(address_columns):

    # Check if address_columns is a single column (string) or multiple columns (list)
    if isinstance(address_columns, str):
        # It's a single column (string), no need to join
        address_str = address_columns
    elif isinstance(address_columns, list):
        # It's a list of columns, join them into a single string
        address_str = ', '.join(address_columns)
    else:
        raise ValueError("Invalid input for address_columns")

    address = {
        'address_line_1': '',
        'address_line_2': '',
        'city': '',
        'state': '',
        'postal_code': ''
    }

    try:
        tagged_address, address_type = usaddress.tag(address_string=address_str, tag_mapping={
            'Recipient': 'recipient',
            'AddressNumber': 'address_line_1',
            'AddressNumberPrefix': 'address_line_1',
            'AddressNumberSuffix': 'address_line_1',
            'StreetName': 'address_line_1',
            'StreetNamePreDirectional': 'address_line_1',
            'StreetNamePreModifier': 'address_line_1',
            'StreetNamePreType': 'address_line_1',
            'StreetNamePostDirectional': 'address_line_1',
            'StreetNamePostModifier': 'address_line_1',
            'StreetNamePostType': 'address_line_1',
            'CornerOf': 'address_line_1',
            'IntersectionSeparator': 'address_line_1',
            'LandmarkName': 'address_line_1',
            'USPSBoxGroupID': 'address_line_1',
            'USPSBoxGroupType': 'address_line_1',
            'USPSBoxID': 'address_line_1',
            'USPSBoxType': 'address_line_1',
            'BuildingName': 'address_line_2',
            'OccupancyType': 'address_line_2',
            'OccupancyIdentifier': 'address_line_2',
            'SubaddressIdentifier': 'address_line_2',
            'SubaddressType': 'address_line_2',
            'PlaceName': 'city',
            'StateName': 'state',
            'ZipCode': 'postal_code',
        })
        for k, v in tagged_address.items():
            address[k] = v
    except usaddress.RepeatedLabelError as e:
        address_type = 'Bad Address'

    # only normalize street address
    # but if you can't then mark as Non-Standard
    if address_type == 'Street Address':
        try:
            address = normalize_address_record(address)
        except:
            address_type = 'Non-Standard'

    # We want a standardize address with a1,a2, city, state, zip, type
    return (
        '' if address['address_line_1'] == None else address['address_line_1'],
        '' if address['address_line_2'] == None else address['address_line_2'],
        '' if address['city'] == None else address['city'],
        '' if address['state'] == None else address['state'],
        '' if address['postal_code'] == None else address['postal_code'],
        address_type
    )

def geocode_address(row):
    # ['physical_address_1', 'physical_address_2', 'physical_city',
    # 'physical_state', 'physical_zip_code', 'geostatus',
    # 'geo_lat', 'geo_lon', 'physical_address_type']
    if row['geostatus'] == 'DONE':
        return (row['geo_lat'], row['geo_lon'], row['geostatus'])

    if row['physical_address_type'] not in ('Street Address',):
        return (row['geo_lat'], row['geo_lon'], row['geostatus'])

    # address = {
    #     'address_line_1': row['physical_address_1'],
    #     'address_line_2': row['physical_address_2'],
    #     'city': row['physical_city'],
    #     'state': row['physical_state'],

    #     'postal_code': row['physical_zip_code']
    # }
    whole = f"{row['physical_address_1']} {row['physical_address_2']}, {row['physical_city']}, {row['physical_state']} {row['physical_zip_code']}"

    location = geolocator.geocode(whole, components=[("administrative_area", row['physical_state'])])

    if location is None:
        return (0.0, 0.0, 'NONE')
    else:
        return (location.latitude, location.longitude, 'NEW')
