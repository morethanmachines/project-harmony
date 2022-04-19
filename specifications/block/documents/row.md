# Vine Row (DRAFT)
A vine row is an arrangement of vines laid out in a linear or [curvilinear](https://en.wikipedia.org/wiki/Curvilinear_coordinates) pattern, with defined row ends so they can be accessed by the headlands and mid rows.

A vine row is a curvilinear feature, it is typically made of posts and wires, as well as vines. It has a canopy, which is the ephemeral extent of the leafy cover of the vines during the growing season.

![Vine row features](https://s3-ap-southeast-2.amazonaws.com/com.platfarm.wordpress/platfarm.com.all/uploads/2020/08/Web_version_Open-Vineyard-Data-Model_Low-Res_web.jpg)  
_Image: Vine Row Features, Source: Collabriculture_

A vine row is typically identified by a ***row number***, with numbering incrementing to traverse the block. However identification systems vary between growers.

A vine row:
* is a child of and contained by exactly one block.
* does not intersect other vine rows or mid rows.
* may not be continuous - for example it may be separated by an obstruction.
* is a parent of any number of vines, typically evenly spaced along it's length.

## Endpoints
The API endpoints required by the block object are:
* POST    **/v1/vinerows**
* GET     **/v1/vinerows/:id**
* POST    **/v1/vinerows/:id**
* GET     **/v1/vinerows**

## The row object
The row object contains the attributes that are described below.

### Attributes
**vine_row_id** `string`  
Unique identifier for the object

**vine_row_parent_id** `string`  
Unique identifier of the object of which this object is a descendant.

**vineyard_id** `string`  
The block in which this row is wholy contained

**block_id** `string`  
The block in which this row is wholy contained

**object** `string, value is vine_row`  
A string representing the object's type. Objects of the same type share the same value.

**merge** `boolean`  
If the the row is being being merged with another row object then `merge` is `true`. If the value of `merge` is not set then it defaults to `false`.

**split** `boolean`  
If the the blockrow is being split then `split` is `true`. If the value of `split` is not set then it defaults to `false`.

**name** `string`  
The descriptive name of the row

**description** `string`  
The row's description. This attribute optionally stores a long form description of the row.

**geometry** `geometry(multilinestring))`  
A [multilinestring](https://geojson.org/geojson-spec.html#id6) collection of [LineString](https://geojson.org/geojson-spec.html#linestring) coordinate arrays providing spatial representation of the block boundaries.

**metadata** `dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a row.

## Create a row

Creates a new row object

`POST /v1/vinerows/`

### Parameters
**block_id** `required`  
The block in which this row is wholy contained

**name** `optional`  
The descriptive name of the row

**description** `optional`  
The row's description. This attribute optionally stores a long form description of the row.

**geometry** `optional)`  
A [multilinestring](https://geojson.org/geojson-spec.html#id6) collection of [LineString](https://geojson.org/geojson-spec.html#linestring) coordinate arrays providing spatial representation of the block boundaries.

**metadata** `optional dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a row. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

## Returns
Returns the vine_row object if the update suceeded. Returns an error if the parameters are invalid. For example, specifying an invalid `block_id`.

## Response
```
{
    "id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
	"object": "vine_row",
	"name": "Row 1",
    "description":"Description of the row",
    "vine_row_parent_id":"",
    "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
    "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
    "geometry": [
        [ [100.0, 0.0], [101.0, 1.0] ],
        [ [102.0, 2.0], [103.0, 3.0] ]
        ],
    "metadata": {
        "key":"value"
    }
}
```

## Retrieve a row
Retrieves a row object

`GET /v1/vinerows/:id`

### Parameters
None

### Returns
Returns a vine row object for a valid system vine row identifier. If it is for a depricated row, the current active block is returned along with it's history.

### Response
```
{
    "id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
	"object": "vine_row",
	"name": "Row 1",
    "description":"Description of the row",
    "vine_row_parent_id":"",
    "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
    "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
    "geometry": [
        [ [100.0, 0.0], [101.0, 1.0] ],
        [ [102.0, 2.0], [103.0, 3.0] ]
        ],
    "metadata": {
        "key":"value"
    },
    "data":[]
}
```

## Update a row
Updates the specified row by setting the values of the parameters passed.

`POST /v1/vinerows/:id`

### Parameters
**vineyard_id** `required`  
The block in which this row is wholy contained

**block_id** `required`  
The block in which this row is wholy contained

**merge** `boolean`  
If the the row is being being merged with another row object then `merge` is `true`. If the value of `merge` is not set then it defaults to `false`.

**split** `boolean`  
If the the row is being split then `split` is `true`. If the value of `split` is not set then it defaults to `false`.

**name** `optional`  
The descriptive name of the row

**description** `optional`  
The row's description. This attribute optionally stores a long form description of the row.

**geometry** `optional multilinestring`  
A [multilinestring](https://geojson.org/geojson-spec.html#id6) collection of [LineString](https://geojson.org/geojson-spec.html#linestring) coordinate arrays providing spatial representation of the block boundaries.

**metadata** `optional dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a row.

### Returns
Returns a dictionary with a `data` property of new row objects if the update succeeded. The row object(s) will all return the parent id of the row from which they were created. When changes are made to a block a new row object is always created. Returns an error if update parameters are invalid (e.g. when `merged` and `split` are both set to true).

### Response
```
{
    "object": "list",
	"url": "/v1/vinerows",
	"type": "split",
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
    "data": [
        {
            "id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
            "object": "vine_row",
            "name": "Row 1",
            "description":"Description of the row",
            "vine_row_parent_id":"",
            "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
            "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
            "geometry": [
                [ [100.0, 0.0], [101.0, 1.0] ],
                [ [102.0, 2.0], [103.0, 3.0] ]
                ],
            "metadata": {
                "key":"value"
            },
            "data":[]
        },
        {
            "id": "g652hgfx-h45n-82jh-jk94-ccf44ng566",
            "object": "vine_row",
            "name": "Row 2",
            "description":"Description of the row",
            "vine_row_parent_id":"",
            "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
            "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
            "geometry": [
                [ [100.0, 0.0], [101.0, 1.0] ],
                [ [102.0, 2.0], [103.0, 3.0] ]
                ],
            "metadata": {
                "key":"value"
            },
            "data":[]
        },       
    ]
}
```

## Delete a row
**It is not possible to delete a row.** Rows can be updated, split and merged but cannot be deleted. This ensures that the provenance of the block is maintained.

`DELETE /v1/vinerows/:id`

### Parameters
None

### Returns
This call returns an error

## List all rows
Returns a list of all vine rows associated with a block. The rows are returned sorted by creation date, with the most recent rows appearing first,

`GET /v1/vinerows`

### Parameters
**vineyard_id** `optional`  
The vineyard in which the vine rows are contained

**block_id** `optional`  
The block in which the vine row objects are wholy contained

**name** `optional`  
The descriptive name of the vine row

**created** `optional`  
A filter on the list based on the object `created` field. The value is a `string` with an `integer` Unix timestamp.

**limit** `optional`  
A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

**starting_after** `optional`   
A cursor for use in pagination. starting_after is an vine row identifier that defines a place in the list. This can be used to page results to improve performance.

### Returns
A dictionary with a data property that contains an array of up to limit vine rows, starting after starting_after. Each entry in the array is a separate vine row object. If no more vine rows are available, the resulting array will be empty. This request should never return an error.

### Response
```
    "object": "list",
	"url": "/v1/vinerows",
	"has_more": false,
	"data":"data": [
        {
            "id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
            "object": "vine_row",
            "name": "Row 1",
            "description":"Description of the row",
            "vine_row_parent_id":"",
            "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
            "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
            "geometry": [
                [ [100.0, 0.0], [101.0, 1.0] ],
                [ [102.0, 2.0], [103.0, 3.0] ]
                ],
            "metadata": {
                "key":"value"
            },
            "data":[]
        },
        {
            "id": "g652hgfx-h45n-82jh-jk94-ccf44ng566",
            "object": "vine_row",
            "name": "Row 2",
            "description":"Description of the row",
            "vine_row_parent_id":"",
            "vineyard_id":"h56873gc-d16a8-4c99-ab25-a489436135ca",
            "block_id":"x569f7fb-c5h3-4k01-ja81-a752166135gc",
            "geometry": [
                [ [100.0, 0.0], [101.0, 1.0] ],
                [ [102.0, 2.0], [103.0, 3.0] ]
                ],
            "metadata": {
                "key":"value"
            },
            "data":[]
        },       
    ]
```