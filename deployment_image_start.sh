# Run the deployment image as a webserver for api calls

docker run -d --name server-pricing-model -p 80:80 server-pricing-model
