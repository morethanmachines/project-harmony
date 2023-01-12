# Wine Australia list of Australian grape vine varieties and their synonyms.

[![Import Latest Australian Grapevine Variety List](https://github.com/morethanmachines/project-harmony/actions/workflows/import-variety-list.yml/badge.svg?branch=main)](https://github.com/morethanmachines/project-harmony/actions/workflows/import-variety-list.yml)

This repository contains an up to date list of Australian grape vine varieties, their synonyms and variety codes as used by Wine Australia.

## Why was this created?
The grape vine varieties list that is maintained here in the Project Harmony repository was created to ensure that a standard, up-to-date list of Australian grape vine variety names and codes were made available to developers with the aim of enhancing interoperability between data sets.

## What is the format of the variety list?

The Australian grape vine varieties, their synonyms and variety codes data set is presented as a JSON file. The JSON (JavaScript Object Notation) is a lightweight data interchange format. It is based on a subset of the JavaScript programming language and is used to transmit data. JSON is a text-based format that uses simple, human-readable text to represent data structures and the data within those structures.

The Australian grape vine variety list JSON file is formatted to the following specification:

```
[{
    "id": "7",
    "prime_name": "Alicante Bouchet",
    "code": "AHB",
    "synonyms": [{
            "name": "Alicante Bouschet",
            "code": "ABS"
        },
        {
            "name": "Alicante Henri Bouschet",
            "code": "AHB"
        }
    ]
}]
```
<details>
    <summary><strong>JSON Schema (click to expand)</strong></summary>
 
 ```
 {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "prime_name": {
          "type": "string"
        },
        "code": {
          "type": "string"
        },
        "synonyms": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "code": {
                  "type": "string"
                }
              },
              "required": [
                "name",
                "code"
              ]
            },
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "code": {
                  "type": "string"
                }
              },
              "required": [
                "name",
                "code"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "prime_name",
        "code",
        "synonyms"
      ]
    }
  ]
}
```
</details>

The specification has been designed to align with and be be in place compatible with previous [collabraculture](https://github.com/CollabricultureOrg/australian-grapevine-varieties/blob/main/data/australian-grape-varieties.json) work in this area*. (*Note that this specification does not include a top 10 flag).

## How often is the list updated?

The list is refreshed in the event of a change in the base grape vine varieties composition list maintained by Wine Australia to support export requirements. The list changes infrequently on a needs basis on average 2 to 3 times a year.

### Process
The process of updating the grape vine varieties and their synonyms list is automated and changes to the list by Wine Australia will be reflected in the Project Harmony repository no later than 24 hours after publication. The process used when updating the variety list is as follows:

<details>
    <summary><strong>Diagram 1. The Variety List Update Process (click to expand)</strong></summary>

    
```mermaid
graph TB
    subgraph Wine Australia
    direction TB
    ChangeFile[Changes made to variety list]-->UploadToSharedDrive{{Changes saved to shared drive as a CSV file}}
    UploadToSharedDrive-->CSVFile>Uploaded CSV File]
    end
    subgraph Github Action
    direction TB
    CheckChanges[Check for changes to the varieties CSV file]-->|Check for changes|CSVFile
    CheckChanges-->HasFileChanged
    HasFileChanged-->|No change|DoNothing[Do nothing]
    DoNothing-->Wait
    HasFileChanged-->|Change|DownloadFile{{Download updated file}}
    DownloadFile-->ProcessFile[Process CSV file]
    ProcessFile-->CommitCSV[Commit updated CSV file]
    ProcessFile-->ApplyTemplate[Apply templates to CSV]
    ApplyTemplate-->CommitFiles[Commit generated files]
    CommitFiles-->Wait[Wait]
    Wait-->CheckChanges
    end
 ```
    
 </details>
 
1. Wine Australia update the Wine Australia internal working varieties dataset.
2. The data is exported as a csv file and saved to a location that is accessible by the Project Harmony GitHub project.
3. A [GitHub action](https://github.com/features/actions) is used to access the raw variety data file daily and a comparison is made of the file to the current version in the Project Harmony repository.
4. If the file has changed then a new version of the file is committed to the Project Harmony repository. The raw CSV file is not developer ready, for example the variety pseudonyms are not extracted. So further processing is required.
5. The file is parsed and converted into developer ready JSON for use (see above formatting).
6. Where required, additional data files may be created to support specific use cases and programming languages.
7. A [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) is raised for the changes to be merged into the main branch.

Through this process, all changes made to the variety list and the generated JSON can be viewed as change sets within GitHub. This ensures that all changes can be communicated as transparently as possible.
