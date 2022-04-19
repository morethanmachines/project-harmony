# Block (DRAFT)
**A block is an area that is planted with rows of vines and is the basic partitioning unit used by grape growers.**

A block represents a collection of rows. These may be spatially located contiguously within the same area or may be split across many distinct spatial areas. It is important to note that blocks are in many cases, a notional management tool and as such may not be visible on the ground.

In most circumstances, a block will partition a single variety but may also be used to partition rows based on other common features such as vintage or soil type.

A block boundary:
* is entirely within one vineyard
* contains a number of vine rows
* does not overlap other blocks
* may be comprised of non contiguous spatial areas

___

## Endpoints
The API endpoints required by the block object are:
* POST    **/v1/blocks**
* GET     **/v1/blocks/:id**
* POST    **/v1/blocks/:id**
* GET     **/v1/blocks**

---

## The block object
The block object contains the attributes that are described below.

### Attributes
**block_id** `string`  
Unique identifier for the object

**parent_id** `string`  
Unique identifier of the object of which this object is a descendant.

**vineyard_id** `string`  
The id of the vineyard containing the block 

**vineyard_block_id** `string`  
Identifier for the object that is provided by the vineyard.

**user_block_id** `string`  
Identifier for the object that is provied by the grower.

**row_spacing** `integer`  
row spacing in millimeters

**created** `timestamp`  
Date and time that the block was created

**object** `string, value is block`  
A string representing the object's type. Objects of the same type share the same value.

**merge** `boolean`  
If the the block is being being merged with another block then `merge` is `true`. If the value of `merge` is not set then it defaults to `false`.

**split** `boolean`  
If the the block is being split then `split` is `true`. If the value of `split` is not set then it defaults to `false`. 

**geometry** `geometry(multipolygon))`  
A [multipolygon](https://geojson.org/geojson-spec.html#id7) collection of [polygon](https://geojson.org/geojson-spec.html#polygon) coordinate arrays providing spatial representation of the block boundaries.

**name** `string`  
The descriptive name of the block

**description** `string`  
The block's description. This attribute optionally stores a long form description of the block for use by the grower.

**metadata** `dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a row.

## Create a block

Creates a new block object

`POST /v1/blocks/`

### Parameters
**vineyard_id** `required`  
The id of the vinyard containing the block.

**parent_id** `optional`  
Unique identifier of the object of which this object is a descendant.

**vineyard_block_id** `optional`  
Identifier for the object that is provided by the vineyard.

**user_block_id** `optional`  
Identifier for the object that is provided by the grower.

**row_spacing** `optional`  
row spacing in millimeters

**geometry** `optional multipolygon`  
A [multipolygon](https://geojson.org/geojson-spec.html#id7) collection of [polygons](https://geojson.org/geojson-spec.html#polygon) providing spatial representation of the block boundaries.

**name** `required`  
The descriptive name of the block

**description** `optional`  
The block's description. This attribute optionally stores a long form description of the block for use by the grower.

**metadata** `optional dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a block.  Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

### Returns
Returns the block object if the update suceeded. Returns an error if the parameters are invalid. For example, specifying an invalid `vineyard_id`.

### Response
```
{
	"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
	"object": "block",
	"name": "Block 1",
	"description": "A description of block 1",
	"created": 1405637071,
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
    "split": false,
	"merged": false,
	"vineyard_block_id": "blk01202022",
	"grower_block_id": "Block by the river",
	"row_spacing": "",
	"geometry": "[ [
		[
			[102.0, 2.0],
			[103.0, 2.0],
			[103.0, 3.0],
			[102.0, 3.0],
			[102.0, 2.0]
		]
	],
	[
		[
			[100.0, 0.0],
			[101.0, 0.0],
			[101.0, 1.0],
			[100.0, 1.0],
			[100.0, 0.0]
		],
		[
			[100.2, 0.2],
			[100.8, 0.2],
			[100.8, 0.8],
			[100.2, 0.8],
			[100.2, 0.2]
		]
	]]"
}
```

## Retrieve a block

`GET /v1/blocks/:id`

### Parameters  
None

### Returns
Returns a block object for a valid block identifier (system, vineyard, user). If it is for a depricated block, the current active block is returned along with `data` property containing a dictionary of the block's parent objects.

### Response
```
{
	"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
	"object": "block",
	"name": "Block 1",
	"description": "A description of block 1",
	"created": 1405637071,
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
    "split": true,
	"merged": false,
	"vineyard_block_id": "blk01202022",
	"grower_block_id": "Block by the river",
	"row_spacing": "",
    "meta_data": {
        "key":"value"
    },
	"geometry": "[ [
		[
			[102.0, 2.0],
			[103.0, 2.0],
			[103.0, 3.0],
			[102.0, 3.0],
			[102.0, 2.0]
		]
	],
	[
		[
			[100.0, 0.0],
			[101.0, 0.0],
			[101.0, 1.0],
			[100.0, 1.0],
			[100.0, 0.0]
		],
		[
			[100.2, 0.2],
			[100.8, 0.2],
			[100.8, 0.8],
			[100.2, 0.8],
			[100.2, 0.2]
		]
	]]",
    "data":[
        {
            "id": "g86fg65-d2d4-7hc6-4466bb-c01275345ca",
            "object": "block",
            "name": "Old Block 1",
            "description": "A description of old block 1",
            "created": 1305637071,
            "parent_id": "",
            "split": true,
            "merged": false,
            "vineyard_block_id": "blk01202021",
            "grower_block_id": "Block by the river",
            "row_spacing": "",
            "meta_data": {
                "key":"value"
            },
            "geometry": "[ [
                [
                    [102.0, 2.0],
                    [103.0, 2.0],
                    [103.0, 3.0],
                    [102.0, 3.0],
                    [102.0, 2.0]
                ]
            ],
            [
                [
                    [100.0, 0.0],
                    [101.0, 0.0],
                    [101.0, 1.0],
                    [100.0, 1.0],
                    [100.0, 0.0]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.8, 0.8],
                    [100.2, 0.8],
                    [100.2, 0.2]
                ]
            ]]"
        }
    ]
}
```

## Update a block
Updates the specified block by setting the values of the parameters passed.

`POST /v1/blocks/:id`

### Parameters  
**vineyard_block_id** `optional`  
Identifier for the object that is provided by the vineyard.

**user_block_id** `optional`  
Identifier for the object that is provied by the grower.

**row_spacing** `optional`  
row spacing in millimeters

**merged** `optional`  
If the the block is being being merged with another block then `merged` is `true`. If the value of `merged` is not set then it defaults to `false`.

**split** `optional`  
If the the block is being split then `split` is `true`. If the value of `split` is not set then it defaults to `false`. 

**geometry** `optional multipolygon`  
A [multipolygon](https://geojson.org/geojson-spec.html#id7) collection of [polygon](https://geojson.org/geojson-spec.html#polygon) coordinate arrays providing spatial representation of the block boundaries.

**name** `optional`  
The descriptive name of the block

**description** `optional`  
The block's description. This attribute optionally stores a long form description of the block for use by the grower.

**metadata** `optional dictionary`  
A set of key-value pairs that can be attached to an object. This can be used for storing additional information about an object in a structured format. For example additional information held by an individual application about a block.  Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

### Returns  
Returns a dictionary with a `data` property of new block objects if the update succeeded. The block object(s) will all return the parent id of the block from which they were created. When changes are made to a block a new block object is always created. Returns an error if update parameters are invalid (e.g. when `merged` and `split` are both set to true).

### Response  
```
{
	"object": "list",
	"url": "/v1/blocks",
	"type": "split",
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
	"data": [{
			"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
			"object": "block",
			"name": "Block 1",
			"description": "A description of block 1",
			"created": 1405637071,
			"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
			"split": true,
			"merged": false,
			"vineyard_block_id": "blk01202022",
			"grower_block_id": "Block by the river",
			"row_spacing": "",
            "meta_data": {
                "key":"value"
            }
			"geometry": "[ [ [
				[102.0, 2.0],
				[103.0, 2.0],
				[103.0, 3.0],
				[102.0, 3.0],
				[102.0, 2.0]
			]
		],
		[
			[
				[100.0, 0.0],
				[101.0, 0.0],
				[101.0, 1.0],
				[100.0, 1.0],
				[100.0, 0.0]
			],
			[
				[100.2, 0.2],
				[100.8, 0.2],
				[100.8, 0.8],
				[100.2, 0.8],
				[100.2, 0.2]
			]
		]
	]
	"
}, {
	"id": "f839f7fb-d1d3-4b33-aa25-c481566135d1",
	"object": "block",
	"name": "Block 1",
	"description": "A description of block 2",
	"created": 1405637071,
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
	"split": true,
	"merged": false,
	"vineyard_block_id": "blk02202022",
	"grower_block_id": "Block by the river",
	"row_spacing": "",
    "meta_data": {
        "key":"value"
    }
	"geometry": "[ [ [
		[102.0, 2.0],
		[103.0, 2.0],
		[103.0, 3.0],
		[102.0, 3.0],
		[102.0, 2.0]
	]
],
[
	[
		[100.0, 0.0],
		[101.0, 0.0],
		[101.0, 1.0],
		[100.0, 1.0],
		[100.0, 0.0]
	],
	[
		[100.2, 0.2],
		[100.8, 0.2],
		[100.8, 0.8],
		[100.2, 0.8],
		[100.2, 0.2]
	]
]]"
}]
}
```

## Delete a block
**It is not possible to delete a block.** Blocks can be updated, split and merged but cannot be deleted. This ensures that the provenance of the block is maintained.

`DELETE /v1/blocks/:id`

### Parameters
None

### Returns
This call returns an error

## List all blocks
Returns a list of all blocks associated with a vineyard. The blocks are returned sorted by creation date, with the most recent blocks appearing first,

`GET /v1/blocks`

## Parameters
**vineyard_id** `required`  
The id of the vineyard containing the block.

**created** `optional`  
A filter on the list based on the object `created` field. The value is  string with an integer Unix timestamp.

**limit** `optional`  
A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

**starting_after** `optional`   
A cursor for use in pagination. starting_after is an block identifier that defines a place in the list. This can be used to page results to improve performance.

### Returns
A dictionary with a data property that contains an array of up to limit blocks, starting after starting_after. Each entry in the array is a separate block object. If no more blocks are available, the resulting array will be empty. This request should never return an error.

### Response
```
{
	"object": "list",
	"url": "/v1/blocks",
	"has_more": false,
	"data": [{
			"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca",
			"object": "block",
			"name": "Block 1",
			"description": "A description of block 1",
			"created": 1405637071,
			"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
			"split": true,
			"merged": false,
			"vineyard_block_id": "blk01202022",
			"grower_block_id": "Block by the river",
			"row_spacing": "",
            "meta_data": {
                "key":"value"
            }
			"geometry": "[ [ [
				[102.0, 2.0],
				[103.0, 2.0],
				[103.0, 3.0],
				[102.0, 3.0],
				[102.0, 2.0]
			]
		],
		[
			[
				[100.0, 0.0],
				[101.0, 0.0],
				[101.0, 1.0],
				[100.0, 1.0],
				[100.0, 0.0]
			],
			[
				[100.2, 0.2],
				[100.8, 0.2],
				[100.8, 0.8],
				[100.2, 0.8],
				[100.2, 0.2]
			]
		]
	]
	"
}, {
	"id": "f839f7fb-d1d3-4b33-aa25-c481566135d1",
	"object": "block",
	"name": "Block 1",
	"description": "A description of block 2",
	"created": 1405637071,
	"parent_id": "1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
	"split": true,
	"merged": false,
	"vineyard_block_id": "blk02202022",
	"grower_block_id": "Block by the river",
	"row_spacing": "",
    "meta_data": {
        "key":"value"
    }
	"geometry": "[ [ [
		[102.0, 2.0],
		[103.0, 2.0],
		[103.0, 3.0],
		[102.0, 3.0],
		[102.0, 2.0]
	]
],
[
	[
		[100.0, 0.0],
		[101.0, 0.0],
		[101.0, 1.0],
		[100.0, 1.0],
		[100.0, 0.0]
	],
	[
		[100.2, 0.2],
		[100.8, 0.2],
		[100.8, 0.8],
		[100.2, 0.8],
		[100.2, 0.2]
	]
]]"
}]
}
```