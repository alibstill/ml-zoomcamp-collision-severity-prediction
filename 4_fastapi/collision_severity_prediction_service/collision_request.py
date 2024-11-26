from pydantic import BaseModel, validator, root_validator
from datetime import datetime, timedelta


class CollisionRequest(BaseModel):
    police_force: str
    number_of_vehicles: int
    day_of_week: str
    time: str
    first_road_class: str
    road_type: str
    speed_limit: int
    light_conditions: str
    weather_conditions: str
    road_surface_conditions: str
    month: str
    day_of_year: int
    is_trunk: int
    is_near_pedestrian_crossing: int
    is_urban: int
    has_special_conditions_at_site: int
    is_carriageway_hazard: int
    is_near_junction: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "police_force": "gloucestershire",
                    "number_of_vehicles": 1,
                    "day_of_week": "tuesday",
                    "time": "04:00",
                    "first_road_class": "a",
                    "road_type": "single_carriageway",
                    "speed_limit": 20,
                    "light_conditions": "darkness___no_lighting",
                    "weather_conditions": "fog_or_mist",
                    "road_surface_conditions": "snow",
                    "month": "january",
                    "day_of_year": 1,
                    "is_trunk": 1,
                    "is_near_pedestrian_crossing": 0,
                    "is_urban": 1,
                    "has_special_conditions_at_site": 1,
                    "is_carriageway_hazard": 0,
                    "is_near_junction": 1,
                }
            ]
        }
    }

    @root_validator(pre=True)
    def check_doy(cls, values):
        month = values.get("month")
        day_of_year = values.get("day_of_year")
        valid_months = [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]

        if month not in valid_months:
            raise ValueError(
                f"Invalid month. Acceptable values: {','.join(valid_months)}"
            )
        start_date = datetime(2023, 1, 1)
        expected_date = start_date + timedelta(days=day_of_year - 1)
        expected_month = expected_date.strftime("%B").lower()

        if expected_month != month:
            raise ValueError(
                "Invalid month and day_of_year combination.Make sure that your day_of_year falls within the month specified. "
                + f"Expected month for {day_of_year}: {expected_month}"
            )

        is_trunk = values.get("is_trunk")
        is_near_pedestrian_crossing = values.get("is_near_pedestrian_crossing")
        is_urban = values.get("is_urban")
        has_special_conditions_at_site = values.get("has_special_conditions_at_site")
        is_carriageway_hazard = values.get("is_carriageway_hazard")
        is_near_junction = values.get("is_near_junction")

        bools = {
            "is_trunk": is_trunk,
            "is_near_pedestrian_crossing": is_near_pedestrian_crossing,
            "is_urban": is_urban,
            "is_trunk": is_trunk,
            "has_special_conditions_at_site": has_special_conditions_at_site,
            "is_carriageway_hazard": is_carriageway_hazard,
            "is_near_junction": is_near_junction,
        }

        is_valid = lambda v: (v == 0) or (v == 1)

        invalid = [k for k, v in bools.items() if not is_valid(v)]
        print(invalid)
        if len(invalid) > 0:
            raise ValueError(
                f"Error with {','.join(invalid)}. This is a boolean. Acceptable values: 0, 1"
            )

        return values

    @validator("road_surface_conditions")
    def road_surface_conditions(cls, road_surface_conditions: str) -> str:
        valid_road_surface_conditions = [
            "wet_or_damp",
            "dry",
            "frost_or_ice",
            "snow",
            "flood_over_3cm._deep",
        ]
        if road_surface_conditions not in valid_road_surface_conditions:
            raise ValueError(
                f"Invalid road_surface_conditions. Acceptable values: {','.join(valid_road_surface_conditions)}"
            )
        return road_surface_conditions

    @validator("weather_conditions")
    def weather_conditions(cls, weather_conditions: str) -> str:
        valid_weather_conditions = [
            "other",
            "fine_no_high_winds",
            "raining_no_high_winds",
            "fine__high_winds",
            "raining__high_winds",
            "snowing_no_high_winds",
            "fog_or_mist",
            "snowing__high_winds",
        ]
        if weather_conditions not in valid_weather_conditions:
            raise ValueError(
                f"Invalid weather_conditions. Acceptable values: {','.join(valid_weather_conditions)}"
            )
        return weather_conditions

    @validator("light_conditions")
    def light_conditions(cls, light_conditions: str) -> str:
        valid_light_conditions = [
            "darkness___lights_lit",
            "daylight",
            "darkness___no_lighting",
            "darkness___lighting_unknown",
            "darkness___lights_unlit",
        ]
        if light_conditions not in valid_light_conditions:
            raise ValueError(
                f"Invalid light_conditions. Acceptable values: {','.join(valid_light_conditions)}"
            )
        return light_conditions

    @validator("speed_limit")
    def speed_limit(cls, speed_limit: int) -> int:
        valid_speed_limit = [20, 30, 40, 50, 60, 70]
        if speed_limit not in valid_speed_limit:
            raise ValueError(
                f"Invalid speed_limit. Acceptable values: {','.join([str(s) for s in valid_speed_limit])}"
            )
        return speed_limit

    @validator("road_type")
    def road_type(cls, road_type: str) -> str:
        valid_road_type = [
            "one_way_street",
            "single_carriageway",
            "roundabout",
            "dual_carriageway",
            "slip_road",
        ]
        if road_type not in valid_road_type:
            raise ValueError(
                f"Invalid road_type. Acceptable values: {','.join(valid_road_type)}"
            )
        return road_type

    @validator("first_road_class")
    def first_road_class(cls, first_road_class: str) -> str:
        valid_first_road_class = ["c", "unclassified", "a", "b", "motorway", "a(m)"]
        if first_road_class not in valid_first_road_class:
            raise ValueError(
                f"Invalid first_road_class. Acceptable values: {','.join(valid_first_road_class)}"
            )
        return first_road_class

    @validator("time")
    def time(cls, time: str) -> str:
        valid_time = [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ]
        if time not in valid_time:
            raise ValueError(
                f"Invalid time. Time is in the form H:M rounded to the nearest hour interval. Acceptable values: {','.join(valid_time)}"
            )
        return time

    @validator("day_of_week")
    def day_of_week(cls, day_of_week: str) -> str:
        valid_dow = [
            "sunday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
        ]
        if day_of_week not in valid_dow:
            raise ValueError(
                f"Invalid day_of_week. Acceptable values: {','.join(valid_dow)}"
            )
        return day_of_week

    @validator("number_of_vehicles")
    def number_of_vehicles(cls, number_of_vehicles: int) -> int:
        if number_of_vehicles == 0:
            raise ValueError(
                f"Invalid number_of_vehicles: At least 1 vehicle must be involved"
            )
        return number_of_vehicles

    @validator("police_force")
    def police_force(cls, police_force: str) -> str:
        valid_police_forces = [
            "metropolitan_police",
            "cumbria",
            "lancashire",
            "merseyside",
            "greater_manchester",
            "cheshire",
            "northumbria",
            "durham",
            "north_yorkshire",
            "west_yorkshire",
            "south_yorkshire",
            "humberside",
            "cleveland",
            "west_midlands",
            "staffordshire",
            "west_mercia",
            "warwickshire",
            "derbyshire",
            "nottinghamshire",
            "lincolnshire",
            "leicestershire",
            "northamptonshire",
            "cambridgeshire",
            "norfolk",
            "suffolk",
            "bedfordshire",
            "hertfordshire",
            "essex",
            "thames_valley",
            "hampshire",
            "surrey",
            "kent",
            "sussex",
            "city_of_london",
            "devon_and_cornwall",
            "avon_and_somerset",
            "gloucestershire",
            "wiltshire",
            "dorset",
            "north_wales",
            "gwent",
            "south_wales",
            "dyfed_powys",
            "police_scotland",
        ]
        if police_force not in valid_police_forces:
            raise ValueError(
                f"Invalid police_force. Acceptable values: {','.join(valid_police_forces)}"
            )
        return police_force
