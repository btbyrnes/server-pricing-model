# Run the deployment image as a webserver for api calls

docker run --rm -d --name server-pricing-model -p 80:80 -p 443:443 server-pricing-model
