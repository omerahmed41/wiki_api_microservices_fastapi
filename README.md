# wiki-api fastapi
##### An API to produce a google-like short description of a person. Example: When you google “yoshua bengio”, you get “Canadian computer scientist” on the right information box as here. Your API will return “Canadian computer scientist” for input “Yoshua bengio”.
## Instructions:
* ### Data source
* - Your source is the English wikipedia page content of the person being asked. For this, you will use the
mediawiki API.
Example : Try the following query for Yoshua Bengio.
https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatver
sion=2&format=json&rvprop=content
You will get a json output which is copied here. You will notice {{Short description|Canadian computer
scientist}} in the content value. 
* - You can use this query as a template and replace titles with the appropriate
input that your API gets.
* #### You will have 48 hours to submit the assignment.



#### For first build:
* make setup
#### To run:
* make run
#### To stop:
* make stop


## Technology Stack & Features:
* Fastapi with python 3.9
* open API and swagger.
* docker with Docker compose.
* makefile.
* Logs.
* REDIS
* Custom exception handler
* CI/CD Pipeline.
* kubernetes.
* Nginx API-gateway.
* Service registry(Eureka Spring Cloud).
* Design patterns (Pub-Sub, Command, Repository, Singleton).
* layer architecture (DDD).


# System Architecture:
![System Architecture](https://user-images.githubusercontent.com/15717941/185804170-07e3266b-a0c8-47b2-b0b7-c506731bb45d.jpg)


## Eureka Service:
#### to see all Instances currently registered with Eureka
* URL: http://localhost:8761
<img width="1435" alt="Screen Shot 2022-08-22 at 2 02 48 AM" src="https://user-images.githubusercontent.com/15717941/185812782-7510305c-25b0-4ffe-b895-d34f88f0c4c8.png">


  
## Docs:
#### I used OpenAPI with swagger for API docs, also  followed Domain driven design with services Layer architecture to make it easy to understand the code
#### Lastly the Naming of Classes, methods and objects is meaningful.

### to test the APIs see: 
#### http://localhost/

We used  swager open-API to auto document your APIs

![Screen Shot 2022-07-04 at 2 21 23 PM](https://user-images.githubusercontent.com/15717941/177135399-ed503896-38f8-4fe0-a41f-1a769fe2d85f.png)

![Screen Shot 2022-07-04 at 2 21 55 PM](https://user-images.githubusercontent.com/15717941/177135458-10933058-acf7-4b25-85cc-8171654363a9.png)


## Design Patterns:
* Pub-Sub: I used bub-sub model along with events streaming broker rabbitmq.
* Repository: Used repository pattern to decouple Domain layer from DB layer, for example we can mock the repository and use DB memory.
* Singleton: Singleton pattern is used by  django for DBConnections.

## CI/CD:
#### Two steps: Build with tests, then Deploy.
#### I commented the part of pushing the images to DockerHub then uploading it to the cloud but, you can easily uncomment that to make it work.
<img width="1440" alt="Screen Shot 2022-08-21 at 6 37 42 PM" src="https://user-images.githubusercontent.com/15717941/185796382-343c44bb-7bbe-4ecc-9b89-49e727d37305.png">

## Todo:
#### the goal was to build the skeleton and base Architecture of the system, but these are Things need to be done when have more time: 
* Review and add more unit, integrations, contracts and acceptance tests.
* Build Frontend with React.js.
* Add more App Validations.
* Focus more on documentation.


* Note make sure you have Docker installed and give it enough memory from the setting