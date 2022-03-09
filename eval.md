# Into Project

Described below is our intro project. Since our service is deployed via Google Cloud services, this project scope, as defined, will expose you to some of day to day cloud service level difficulty you may face beyond the python programing. 

The goal of the into project is:

- Expose and see how you are able absorb 
  - Google Cloud Services
  - FastAPI
- Get a feel for you programming style/testing/design
- Give you a taste of the fast passed expectations of having to quickly learn new services and frameworks.
- Give you a chance to determine if this kind of work is not for you :)

## Project Overview

Create/deploy a cloud run service that integrates with Firebase Firestore and has an API to increment counts for user provided `tags` and an api to retrieve 


### Service API Endpoints

#### Increment Count

Create an endpoint that can receive a JSON body payload request that contains a `tag` **name** and **value**. 
- This value is to be added to the current value stored for that `tag` (default start being 0). 
- The `tag` **name** will be a string that conforms to `[a-z_]{3,15}`
- The value can be any positive integer (less than 10)

Example of payload

```json
{
   "name":"foo",
   "value":4
}

```

#### Get Tag Stats

Create an endpoint that will return the current incremented counts for all stored tags. 

- Return the list of tags that have been provided to the increment count endpoint defined above. 
- For each tag return the sum of all of the increment values.
- Return the list as a JSON body

Example of response

```json
{
  "foo": 13,
  "ballz": 76,
  ...
}
```

### Cloud Run

The service **MUST** be deployed as a container via [Google's Cloud Run Managed Service](https://cloud.google.com/run/docs).

### FastAPI

The service **MUST** use the FastAPI web framework. You may design the code structure as you see fit, however please layout your files and classes in a way that would maximize clarity for other members of the development team.

### JSON Schema

The FastAPI service **MUST** produce a wellformed and verbose [OpenAPI 3.0 Schema](https://swagger.io/docs/specification/about/) that clearly describes the service and endpoints.

### FireStore Storage

The tag data is to be stored in FireBase's Firestore
- You can select how you feel the data should be structured and into what type of document collection and how many documents.
- Pay careful consideration to the scalability of the service.
  - How many requests a second could this handle?
  - How many unique tags could this handle?
  
### CloudWatch Logs

The service's logs should be formatted to be compliant with [Stackdriver structured logs](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry), including the trace value

### StackDriver Metric

Create a [StackDriver Log-Based Metric](https://cloud.google.com/logging/docs/logs-based-metrics) that is the sum of the counts provided to the api in the increment count endpoint.

### Testing

We believe good testing is very important, however we are not declaring specific testing requirements other than all external APIs should all be verified by unit testing. Testing other than these may be included as you see fit e.g. pytext, mocks ;)


### Other Considerations

- You may assume that these endpoints are public and do not require any auth.
- Use any CloudRun configurations you would like.


### Google Cloud Project Access

Create a new GCP account if you do not have one yet. This entire project can be completed with no charge with a Google Cloud account since all usage would be within the free usage tier.
