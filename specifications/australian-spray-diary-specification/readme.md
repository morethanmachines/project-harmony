# Spray Diary Specification


| Field | Type | Description | 
| :---- | :---- | :--------- | 
| schema_version | `float` | Version of the data schema used | 
| records | `array` | An `array` of records containing information about the application | 
| record_id | `string` | Unique identifier for the application record | 
| start_time | `string` | Date and time when the application started | 
| end_time | `string` | Date and time when the application ended | 
| operator | `string` | Name of the operator who applied the product | 
| blocks | `array` | An `array` of blocks to which the product was applied | 
| block_id | `string` | Unique identifier for the block | 
| variety_code | `string` | Code for the grape variety to which the product was applied | 
| growth_stage | `integer` | Growth stage of the grapevines when the product was applied | 
| comment | `string` | Any additional comments about the application | 
| products_applied | `array` | An `array` containing information about the product that was applied | 
| product_name | `string` | Name of the product that was applied | 
| type | `string` | Type of the product (fungicide, pesticide, fertilizer) | 
| chemical | `string` | Name of the active ingredient in the product | 
| formulation | `string` | Formulation of the product (liquid, powder) | 
| apvma_id | `string` | Unique identifier for the product, assigned by the Australian Pesticides and Veterinary Medicines Authority | 
| target | `string` | Target pest or disease for which the product was applied | 
| usage_restrictions | `array` | An `array` of | `object` |s containing usage restrictions for the product | 
| type | `string` | Type of usage restriction (winery, industry) | 
| reference | `string` | Reference to the organization or entity that issued the usage restriction | 
| unit | `string` | Unit of measurement for the usage restriction | 
| value | `integer` | Numeric value of the usage restriction | 
| label_rate_per_100l | `object` | An `object` containing information about the label rate per 100L | 
| user_product_unit | `string` | User-specified unit for the product | 
| user_dilution_unit | `string` | User-specified unit for the dilution | 
| user_product_amount | `string` | User-specified amount of the product | 
| user_dilution_amount | `string` | User-specified amount of the dilution | 
| metric_product_amount | `string` | Metric amount of the product | 
| metric_dilution_amount | `string` | Metric amount of the dilution | 
| concentration_factor | `integer` | Concentration factor of the product | 
| water_sprayed | `object` | An `object` containing information about the amount of water sprayed | 
| user_distance_unit | `string` | User-specified unit of distance | 
| user_distance | `integer` | User-specified distance sprayed | 
| user_volume_unit | `string` | User-specified unit of volume | 
| user_volume_sprayed | `integer` | User-specified volume of water sprayed | 
| metric_distance | `integer` | Metric distance sprayed | 
| metric_volume_sprayed | `integer` | Metric volume of water sprayed | 
| registered_product_used | `object` | An `object` containing information about the amount of product used | 
| user_distance_unit | `string` | User-specified unit of distance | 
| user_distance | `integer` | User-specified distance covered | 
| user_product_unit | `string` | User-specified unit of the product | 
| user_volume_applied | `float` | User-specified volume of the product applied | 
| metric_distance | `integer` | Metric distance covered | 
| metric_volume_applied | `float` | Metric volume of the product applied |
| weather_condition_records	| `array` |	An `array` of objects containing weather condition records | 
| lattitude	| `string` |	Latitude of the location where the weather was recorded. | 
| longitude	| `string` |	Longitude of the location where the weather was recorded. | 
| wind_speed_unit	| `string` |	Unit of measurement for the wind speed. | 
| wind_speed	| `integer` |	Wind speed recorded during the time period. | 
| wind_direction	| `string` |	Direction the wind is blowing from. | 
| temperature_unit	| `string` |	Unit of measurement for the temperature. | 
| temperature_value	| `float` |	Temperature recorded during the time period. | 
| humidity_unit	| `string` |	Unit of measurement for the humidity. | 
| humidity_value	| `integer` |	Humidity recorded during the time period. | 
| precipitation_unit	| `string` |	Unit of measurement for the precipitation. | 
| precipitation_value	| `float` |	Amount of precipitation recorded during the time period.
