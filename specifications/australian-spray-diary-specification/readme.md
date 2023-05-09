# Spray Diary Specification

**Note:** While the specification is being tested with industry we expect that there will be serveral, potentially breaking changes to the format. The specification is versioned to support this. Once a version 1 of the specification is reached through industry testing future changes will be released through a defined release process managed by Wine Australia maintainers.

# Overview 
This spray diary specification outlines a proposed format for recording and reporting spray applications in the Australian viticulture industry. It is intended for use by those who are already familiar with the concept of a spray diary.

The spray diary specification includes detailed information about each spray application, including the start and end times, the operator responsible for the application, the blocks of land treated, the variety of grapes, and the growth stage of the vines. Additionally, the specification includes information on the chemical products used, including the product name, type, chemical composition, formulation, and target pest or disease. Restrictions on product usage are also recorded, including any required withholding periods and usage restrictions specific to the winery or the industry at large.

To ensure accuracy in record keeping, this specification also includes recording of data on the weather conditions at the time of the application, such as wind speed and direction, temperature, humidity, and precipitation. This information is important for assessing the effectiveness of the application and determining whether additional applications are necessary. It also records environmental evidence of application timing to support data pertaining to spray drift events.

The JSON specification document can be found [here](https://github.com/morethanmachines/project-harmony/blob/main/specifications/australian-spray-diary-specification/spray-diary.json)


### Example use cases

Its is expected that the spray diary specification will support at least two existing use cases. 

The first use case is where spray diary information collected by a grower is eported from an existing system. This activity is currently achieved in the most part through the use of CSV files created using different column naming structures. This makes it diffiult for growers to merge spray diaries exported from different systems and requires third parties whom consume the data to implement multiple import pipelines to prepare imported data for use. The common specification presented here is designed to mitigate this by providing an opinionated, co-created structure against which parties can align their data.

The second use case for the specification is for the transmission of data directly from system to system via APIs. In this example, we will describe the process of sending spray diary data from a data provider to a data receiver's API endpoint. The data will be transmitted in the JSON format defined in the specification, and the provider will need to authenticate with the endpoint using the authentication method required by the specific endpoint. It's important to note that the authentication method may vary from receiver to receiver, but for this example, we will use OAuth 2.0. An example API process has been outlined in more detail below to illustrate the use of the spray diary data specification.

### Process Overview

**Data Provider Preparation**
- Ensure the spray diary data is aligned to the specification, containing all the required attributes.
- Implement OAuth 2.0 authentication logic and obtain the necessary access tokens for API communication.
- Understand the API documentation provided by the data receiver to identify the required endpoint and authentication method.

**Authentication**
- Retrieve the OAuth 2.0 client credentials (client ID and client secret) from the data receiver's authentication portal or API documentation.
- Implement the OAuth 2.0 authentication flow in the data provider's application, following the receiver's specific authentication requirements.
- This process typically involves exchanging the client credentials for an access token by sending a token request to the receiver's authorization server.

**Data Transmission**
- Once authenticated, construct the JSON payload containing the viticulture spray diary data to be sent to the API endpoint.
- Include all the necessary attributes required by the receiver, ensuring the data adheres to the receiver's defined data schema or specifications.
- Utilise the appropriate HTTP methods (e.g., POST, PUT, or PATCH) to send the data to the reciever's API endpoint.
- Set the appropriate headers, including the Content-Type header specifying that the payload is in JSON format.

**Error Handling and Responses**
- Handle any potential errors that may occur during the API request, such as network issues, invalid requests, or authentication failures.
- Monitor and interpret the responses received from the API endpoint, considering both successful responses and error responses.
- Implement appropriate error handling mechanisms to retry failed requests, handle rate limiting, and ensure data integrity.

### Use Case Example
Suppose a grower wants to use their pray diary data to support their sustainability credentials. The grower, using their vinyard management application, collects spray diary information from their various spray application activities and sends it to their industry sustainability auditor's API endpoint so that their claims can be validated and used to sell into markets requiring sustainability credentials.

Their vinyard management system implements OAuth 2.0 authentication to authenticate with the industry auditor's API endpoint. They obtain the client credentials (client ID and client secret) from the indstry sustainability auditor's authentication portal. Following the OAuth 2.0 flow, their vineyard management software exchanges these credentials for an access token.

Once authenticated, the provider constructs a JSON payload containing the spray diary data in the format outlined in the specification, including attributes such as vineyard ID, spray date, chemicals used, dosage, and application method etc. They send a POST request to the auditor's API endpoint, setting the appropriate headers and including the JSON payload.

The vineyard management software handles any potential errors, such as network failures or authentication errors, and retries failed requests if necessary. They monitor the API responses, verifying that the data is successfully received and processed by the auditor's system.






