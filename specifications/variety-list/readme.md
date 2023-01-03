# Wine Australia Variety List

This repository contains an up to date list of varieties and variety codes as used by Wine Australia.

The list is refreshed in the event of a change in the base variety list maintained by Wine Australia.

The process used when updating the variety list is as follows:

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

All changes made in the files can be viewed as change sets within github.
