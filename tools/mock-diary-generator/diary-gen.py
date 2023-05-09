import random
from datetime import datetime, timedelta
import json
import uuid
import string
import urllib.request

def random_vineyard_name():
    words = ['vineyard', 'winery', 'cellars', 'estates', 'farms', 'ranches', 'vines', 'fields', 'orchards']
    random.shuffle(words)
    name = ' '.join(words[:random.randint(2, 3)])
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def random_product_type():
    return random.choice(["fungicide", "pesticide", "fertiliser", "herbicide", "insecticide", "adjuvents"])

def random_address():
    street_names = ["Main", "High", "King", "Queen", "George", "Park", "Victoria", "Prince", "Albert", "Charles"]
    street_types = ["Street", "Road", "Avenue", "Lane", "Drive", "Boulevard", "Place", "Crescent", "Terrace", "Parade"]
    suburbs = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle", "Canberra", "Sunshine Coast", "Geelong"]
    states = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "NT", "ACT"]
    postcode = str(random.randint(2000, 9999))
    street_number = str(random.randint(1, 999))
    street_name = random.choice(street_names)
    street_type = random.choice(street_types)
    suburb = random.choice(suburbs)
    state = random.choice(states)
    return (
        f"{street_number} {street_name} {street_type}", 
        suburb, 
        state, 
        postcode
    )

def random_name():
    first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila', 'Aria', 'Scarlett']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson']
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def random_dates():
    start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
    end_date = start_date + datetime.timedelta(days=random.randint(7, 21))
    return start_date.strftime('%Y-%m-%dT%H:%M:%SZ'), end_date.strftime('%Y-%m-%dT%H:%M:%SZ')

def random_entry_dates():
    earliest_date = datetime.strptime('2000-01-01T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
    latest_date = datetime.utcnow()
    total_seconds = (latest_date - earliest_date).total_seconds()
    created_date = earliest_date + timedelta(seconds=random.randint(0, int(total_seconds)) if total_seconds > 0 else 0)
    created_total_seconds = (latest_date - created_date).total_seconds()
    last_modified_date = created_date + timedelta(seconds=random.randint(1, int(created_total_seconds)) if created_total_seconds > 0 else 1)
    modified_total_seconds = (latest_date - last_modified_date).total_seconds()
    submission_date = last_modified_date + timedelta(seconds=random.randint(1, int(modified_total_seconds)) if modified_total_seconds > 0 else 1)
    submission_total_seconds = (submission_date - created_date).total_seconds()
    session_start = created_date + timedelta(seconds=random.randint(1, int(submission_total_seconds)) if submission_total_seconds > 0 else 1)
    session_total_seconds = (last_modified_date - session_start).total_seconds()
    session_end = session_start + timedelta(seconds=random.randint(1, int(session_total_seconds)) if session_total_seconds > 0 else 1)

    return (
        created_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        last_modified_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        submission_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        session_start.strftime('%Y-%m-%dT%H:%M:%SZ'),
        session_end.strftime('%Y-%m-%dT%H:%M:%SZ')
    )

def random_abn():
    abn = ''
    for i in range(11):
        if i == 2 or i == 5:
            abn += ' '
        else:
            abn += str(random.randint(0, 9))
    return abn

def random_chemical_product_name():
    company_prefix = ['Aqua', 'Bio', 'Chroma', 'Dura', 'Eco', 'Flux', 'Glow', 'Hydro', 'Inno', 'Jade', 'Klear', 'Luma', 'Max', 'Natura', 'Ozone', 'Penta', 'Quantum', 'Revo', 'Sola', 'Terra', 'Ultra', 'Vista', 'Wav', 'Xenon', 'Yotta', 'Zen']
    company_suffix = ['tech', 'lab', 'chem', 'corp', 'industries', 'solutions', 'systems', 'science', 'gen', 'tech', 'materials', 'products', 'pharma', 'health', 'innovations', 'inc', 'bio', 'chemicals', 'dynamics', 'tech', 'supplies', 'global', 'pioneer', 'fusion', 'technologies', 'sciences']
    chem_prefix = ['hydro', 'meth', 'chloro', 'eth', 'diox']
    chem_suffix = ['ane', 'ene', 'ide', 'ate', 'ol']
    product_name = random.choice(company_prefix) + random.choice(company_suffix) + ' ' + random.choice(chem_prefix) + random.choice(chem_suffix)
    return product_name

def random_chemical():
    return random_chemical_product_name()

def random_lat_long():
    lat = round(random.uniform(-90, 90), 6)
    lon = round(random.uniform(-180, 180), 6)
    return (lat, lon)

def random_wind_direction():
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return random.choice(directions)

def random_pest():
    pest_types = ['Cape Weed', 'Grapevine Moth', 'Mealybugs', 'Phylloxera', 'Powdery Mildew', 'Red Spider Mite', 'Vine Mealybug', 'Vine Thrips']
    return random.choice(pest_types)

def random_active_ingredient():
    active_ingredients = ['Bifenthrin', 'Chlorpyrifos', 'Cypermethrin', 'Fipronil', 'Imidacloprid', 'Lambda-cyhalothrin', 'Malathion', 'Permethrin']
    return random.choice(active_ingredients)

def get_grapevine_varieties():
    url = "https://raw.githubusercontent.com/morethanmachines/project-harmony/main/specifications/australian-grapevine-variety-list/variety-list/json/variety-list.json"  # replace with the actual URL of your JSON file
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def get_random_prime_name(varieties):
    prime_names = [d["prime_name"] for d in varieties]
    return random.choice(prime_names)


varieties = get_grapevine_varieties()

records = {}

record_dates = random_entry_dates()
vinyard_address = random_address()
operator_address = random_address()

def gen_observations():
    #Generate some weather observations
    observations = []
    for i in range(random.randint(1, 100)):
        latlon = random_lat_long()
        dates = random_entry_dates()
        observation = {
            "record_id":str(uuid.uuid4()),
            "record_start":dates[3],
            "record_end":dates[4],
            "lattitude":latlon[0],
            "longitude":latlon[1],
            "wind_speed_unit":"m/s",
            "wind_speed":random.randint(1, 100),
            "wind_direction":random_wind_direction(),
            "temperature_unit":random.choice(["celcius","farenheit"]),
            "temperature_value":random.randint(0, 45),
            "humidity_unit":"%",
            "humidity_value":random.randint(1, 100),
            "precipitation_unit":"millimeters",
            "precipitation_value":random.randint(1, 50)
        }
        observations.append(observation)
    return observations

def gen_products():
    #Generate some products
    products = []
    for i in range(random.randint(1, 10)):
        product = {
            "product_name":random_chemical_product_name(),
            "type":random_product_type(),
            "chemical":random_chemical(),
            "formulation":random.choice(["liquid", "powder"]),
            "active_ingredient":random_active_ingredient(),
            "apvma_id":''.join(random.choice(string.digits) for i in range(5)),
            "target":random_pest(),
            "sprary_width_unit":"meters",
            "spray_width": 1.5,
            "usage_restrictions":[
                {
                    "type":"industry",
                    "reference":"AWRI",
                    "unit":"el",
                    "value":29
                },
                {
                    "type":"winery",
                    "reference":"Accolade",
                    "unit":"days",
                    "value":30
                },
                {
                    "type":"industry",
                    "reference":"AWRI",
                    "unit":"days",
                    "value":30
                }
            ],
            "label_rate_per_100l":{
                "user_product_unit":"litres",
                "user_dilution_unit":"litres",
                "user_product_amount":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                "user_dilution_amount":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                "metric_product_amount":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                "metric_dilution_amount":random.choice([0.5, 1, 2, 2.5, 5, 10])
            },
            "concentration_factor":random.randint(1, 5),
            "water_sprayed": {
                "user_distance_unit":random.choice(["hectare","meters"]),
                "user_distance":random.randint(100, 5000),
                "user_volume_unit":"litres",
                "user_volume_sprayed":random.randint(100, 5000),
                "metric_distance":random.randint(100, 5000),
                "metric_volume_sprayed":random.randint(100, 5000)
            },
            "registered_product_used":{
                "user_distance_unit":random.choice(["hectare","meters"]),
                "user_distance":random.randint(100, 5000),
                "user_product_unit":random.choice(["kg","g","ml","l"]),
                "user_volume_applied":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                "label_rate":{
                    "min":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                    "max":random.choice([0.5, 1, 2, 2.5, 5, 10])
                },
                "metric_distance":random.randint(100, 5000),
                "metric_volume_applied":random.choice([0.5, 1, 2, 2.5, 5, 10]),
                "row_width_unit": "meters",
                "row_width": 10
            }
        }
        products.append(product)
    return products

def gen_records(record_count):
    #Generate some records
    records = []
    for i in range(record_count):
        record = {
                    "record_id":str(uuid.uuid4()),
                    "created_date":record_dates[0],
                    "last_modified_date":record_dates[1],
                    "submission_date":record_dates[2],
                    "session_start":record_dates[3],
                    "session_end":record_dates[4],
                    "version_number": 1,
                    "vintage":random.randint(2000, 2023),
                    "submitted":random.choice(['true', 'false']),
                    "vinyard": {
                        "business_name":random_vineyard_name(),
                        "business_abn":random_abn(),
                        "business_address":vinyard_address[0],
                        "business_postcode":vinyard_address[3],
                        "business_state":vinyard_address[2]
                    },
                    "operator": {
                        "name":random_name(),
                        "address":operator_address[0],
                        "postcode":operator_address[3],
                        "state":operator_address[2],
                        "phone":""
                    },
                    "blocks":"",
                    "variety_code":"BRC",
                    "variety_name":get_random_prime_name(varieties),
                    "growth_stage_el":random.randint(1, 47),
                    "comment":"",
                    "wine_company_comment":"",
                    "products_applied": gen_products(),
                    "weather_condition_records":gen_observations()
                }
        records.append(record)
    return records

def gen_diary(records):
    print(f'Generating a spray diary with {records} records.')
    diary = {
        "$schema": "https://raw.githubusercontent.com/morethanmachines/project-harmony/main/specifications/australian-spray-diary-specification/spray-diary-schema.json",
        "version":1.0,
        "records":gen_records(records)
    }

    with open("diary.json", "w") as diary_file:
        json.dump(diary, diary_file, indent=2)




#Generate the diary with 10 entries
gen_diary(100000)