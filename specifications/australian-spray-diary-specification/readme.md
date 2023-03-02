# Spray Diary Specification


| Field | Data | Type | Description | | 
| :-- | :-- | :-- | :-- |  | 
| schema_version | `float` | Version of the data schema used | 
| records | `array` | An | `array` | of records containing information about the application | 
| record_id | `string` | Unique identifier for the application record | 
| start_time | `string` | Date and time when the application started | 
| end_time | `string` | Date and time when the application ended | 
| operator | `string` | Name of the operator who applied the product | 
| blocks | `array` | An | `array` | of blocks to which the product was applied | 
| block_id | `string` | Unique identifier for the block | 
| variety_code | `string` | Code for the grape variety to which the product was applied | 
| growth_stage | `integer` | Growth stage of the grapevines when the product was applied | 
| comment | `string` | Any additional comments about the application | 
| products_applied | `object` | An | `object` | containing information about the product that was applied | 
| product_name | `string` | Name of the product that was applied | 
| type | `string` | Type of the product (fungicide, pesticide, fertilizer) | 
| chemical | `string` | Name of the active ingredient in the product | 
| formulation | `string` | Formulation of the product (liquid, powder) | 
| apvma_id | `string` | Unique identifier for the product, assigned by the Australian Pesticides and Veterinary Medicines Authority | 
| target | `string` | Target pest or disease for which the product was applied | 
| usage_restrictions | `array` | An | `array` | of | `object` |s containing usage restrictions for the product | 
| type | `string` | Type of usage restriction (winery, industry) | 
| reference | `string` | Reference to the organization or entity that issued the usage restriction | 
| unit | `string` | Unit of measurement for the usage restriction | 
| value | `integer` | Numeric value of the usage restriction | 
| label_rate_per_100l | `object` | An | `object` | containing information about the label rate per 100L | 
| user_product_unit | `string` | User-specified unit for the product | 
| user_dilution_unit | `string` | User-specified unit for the dilution | 
| user_product_amount | `string` | User-specified amount of the product | 
| user_dilution_amount | `string` | User-specified amount of the dilution | 
| metric_product_amount | `string` | Metric amount of the product | 
| metric_dilution_amount | `string` | Metric amount of the dilution | 
| concentration_factor | `integer` | Concentration factor of the product | 
| water_sprayed | `object` | An | `object` | containing information about the amount of water sprayed | 
| user_distance_unit | `string` | User-specified unit of distance | 
| user_distance | `integer` | User-specified distance sprayed | 
| user_volume_unit | `string` | User-specified unit of volume | 
| user_volume_sprayed | `integer` | User-specified volume of water sprayed | 
| metric_distance | `integer` | Metric distance sprayed | 
| metric_volume_sprayed | `integer` | Metric volume of water sprayed | 
| registered_product_used | `object` | An | `object` | containing information about the amount of product used | 
| user_distance_unit | `string` | User-specified unit of distance | 
| user_distance | `integer` | User-specified distance covered | 
| user_product_unit | `string` | User-specified unit of the product | 
| user_volume_applied | `float` | User-specified volume of the product applied | 
| metric_distance | `integer` | Metric distance covered | 
| metric_volume_applied | `float` | Metric volume of the product applied |


weather_condition_records	array	An array of objects containing weather condition records
record_id	string	Unique identifier for the weather condition record
record_start	string	Date and time when the weather condition record started
record_end	string	Date and time when the weather condition record
block_id	string	The unique identifier for the block within the vineyard.
variety_code	string	The code representing the grape variety being grown.
growth_stage	integer	The growth stage of the grapes, as defined by a standardized system.
comment	string	Any additional comments or notes related to the application of the products.
product_name	string	The name of the product that was applied to the grapes.
type	string	The type of product that was applied (e.g. fungicide, pesticide, fertilizer).
chemical	string	The active chemical ingredient in the product.
formulation	string	The form in which the product was applied (e.g. liquid, powder).
apvma_id	string	The registration number of the product with the relevant government agency.
target	string	The pest or disease that the product was intended to control.
usage_restrictions	array of objects	Any restrictions or limitations on the use of the product, specified by type of user, reference, unit, and value.
user_product_unit	string	The unit of measure for the product amount specified by the user.
user_dilution_unit	string	The unit of measure for the dilution specified by the user.
user_product_amount	string	The amount of product specified by the user.
user_dilution_amount	string	The amount of dilution specified by the user.
metric_product_amount	string	The amount of product converted to metric units.
metric_dilution_amount	string	The amount of dilution converted to metric units.
concentration_factor	integer	The ratio of product to water used in the spray.
user_distance_unit	string	The unit of measure for the user-specified distance.
user_distance	integer	The distance the user specified for the area sprayed.
user_volume_unit	string	The unit of measure for the volume of spray applied.
user_volume_sprayed	integer	The volume of spray applied specified by the user.
metric_distance	integer	The distance converted to metric units.
metric_volume_sprayed	integer	The volume of spray applied converted to metric units.
registered_product_used	object	Information about the registered product used to create the spray.
metric_distance	integer	The distance converted to metric units.
metric_volume_applied	integer	The volume of the registered product applied converted to metric units.
record_id	string	Unique identifier for the weather condition record.
record_start	string (timestamp)	Start time of the weather record.
record_end	string (timestamp)	End time of the weather record.
lattitude	string	Latitude of the location where the weather was recorded.
longitude	string	Longitude of the location where the weather was recorded.
wind_speed_unit	string	Unit of measurement for the wind speed.
wind_speed	integer	Wind speed recorded during the time period.
wind_direction	string	Direction the wind is blowing from.
temperature_unit	string	Unit of measurement for the temperature.
temperature_value	float	Temperature recorded during the time period.
humidity_unit	string	Unit of measurement for the humidity.
humidity_value	integer	Humidity recorded during the time period.
precipitation_unit	string	Unit of measurement for the precipitation.
precipitation_value	float	Amount of precipitation recorded during the time period.
