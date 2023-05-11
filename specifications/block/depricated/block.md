# Block (DRAFT)
A block is an area that is planted with rows of vines and is the basic partitioning unit used by grape growers.

A block represents a collection of rows. These may be spatially located contiguously within the same area or may be split across many distinct spatial areas. It is important to note that blocks are in many cases, a notional management tool and as such may not be visible on the ground.

In most circumstances, a block will partition a single variety but may also be used to partition rows based on other common features such as vintage or soil type.

A block boundary:
* is entirely within one vineyard
* contains a number of vine rows
* does not overlap other blocks
* may be comprised of non contiguous spatial areas

## Endpoints
The API endpoints required by the block object are:
* POST    /v1/blocks
* GET     /v1/blocks/:id
* POST    /v1/blocks/:id
* GET     /v1/blocks

| URI | Post | Get | Put |
| --- | --- | --- | --- |
| /v1/blocks | Create a new block | Retrieve all blocks | bulk update |
| /v1 /blocks/1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a | Error | Get details of block | Update details of block |

## The block object
The block object contains the attributes that are described below.
### Attributes
---
**block_id** `string`  
Unique identifier for the object

**parent_id** `string`  
Unique identifier of the object of which this object is a descendant.

**vineyard_id** `string`  
The id of the vineyard containing the block 

**vineyard_block_id** `string`  
Identifier for the object that is provided by the vineyard.

**grower_block_id** `string`  
Identifier for the object that is provied by the grower.

**row_spacing** `integer`  
row spacing in millimeters

**created** `timestamp`  
Date and time that the block was created

**object** `string, value is block`  
A string representing the object's type. Objects of the same type share the same value.

**geometry** `geometry(multipolygon)`  
A collection of polygon coordinate arrays providing spatial representation of the block boundaries.

**name** `string`  
The descriptive name of the block

**description** `string`  
The block's description. This attribute optionally stores a long form description of the block for use by the grower.

## Create a block

Creates a new block object

`POST /v1/blocks/`

### Parameters
**vineyard_id** `required`  
The id of the vinyard containing the block.

**parent_id** `optional`  
Unique identifier of the object of which this object is a descendant.

**vineyard_block_id `optional`  
Identifier for the object that is provided by the vineyard.

**grower_block_id `optional`  
Identifier for the object that is provided by the grower.

**row_spacing** `optional`  
row spacing in millimeters

**geometry** `optional`  
A collection of polygons providing spatial representation of the block boundaries.

**name** `optional`  
The descriptive name of the block

**description** `optional`  
The block's description. This attribute optionally stores a long form description of the block for use by the grower.

### Returns
Returns the block object if the update suceeded. Returns an error if the parameters are invalid. For example, specifying an invalid `vineyard_id`.

### Response
`{
"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca", 
"object": "block",
"name": "Block 1",
"description": "A description of block 1",
"created": 1405637071,
"parent_id":"1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
"vineyard_block_id":"blk01202022",
"grower_block_id":"Block by the river",
"row_spacing":"",
"geometry":"[
      [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]], [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],[[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]]"
}`

## Retrieve a block

### Parameters  
No parameters

### Returns
Returns a block object for a valid block identifier. If it is for a depricated block, the current active block is returned along with it's history.

### Response
`{
"id": "f839f7fb-d1d3-4b33-aa25-c481566135ca", 
"object": "block",
"name": "Block 1",
"description": "A description of block 1",
"created": 1405637071,
"parent_id":"1e6a46fe-9c9c-4439-b1c0-1ff1794cb17a",
"vineyard_block_id":"blk01202022",
"grower_block_id":"Block by the river",
"row_spacing":"",
"geometry":"[
      [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]], [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],[[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]]"
}`

## Update a block
Updates the specified block by setting the values of the parameters passed.

### Parameters  
TBC

### Returns  
Returns the block object if the update succeeded. Returns an error if update parameters are invalid (e.g. specifying an invalid parent_id).

### Reponse  
TBC

## Delete a block
It is not possible to delete a block. Blocks can be updated to be split and merged but cannot be deleted.

### Parameters
None

### Returns
This call returns an error

## List all blocks
Returns a list of all blocks associated with a vineyard. The blocks are returned sorted by creation date, with the most recent blocks appearing first,

## Parameters
**vineyard_id** `required`  
The id of the vineyard containing the block.

**created** `optional`  
The id of the vineyard containing the block.
A filter on the list based on the object `created` field. The value is  string with an integer Unix timestamp.

**limit** `optional`  
A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

**starting_after** `optional`   
A cursor for use in pagination. starting_after is an block identifier that defines a place in the list. This can be used to page results to improve performance.

### Returns
A dictionary with a data property that contains an array of up to limit blocks, starting after starting_after. Each entry in the array is a separate block object. If no more blocks are available, the resulting array will be empty. This request should never return an error.