#!/bin/bash

resourcegroup='LinkedinBioGen'
location='westeurope'
registry='linkedinbioregistry'
container='linkedin'
appserviceplan='linkedinbiogenserviceplan'
webappname='linkedin-bio-gen-app'

echo "Uploading app to Azure..."
echo "Creating Resource Group"
az group create -n $resourcegroup -l $location

echo "Creating Container Registry"
if [ $? -eq 0 ]; then 
    az acr create -g $resourcegroup -n $registry --sku Basic
    az acr login -n $registry
else
    echo 'Error'
    exit 1
fi 

echo "Building Docker container"
if [ $? -eq 0 ]; then 
    az acr build -r $registry -g $resourcegroup -t "${container}:latest" .
    az acr repository -n $registry
else   
    echo 'Error'
    exit 1
fi 

echo "Creating app servic plan"
if [ $? -eq 0 ]; then 
    az appservice plan create --name $appserviceplan --resource-group $resourcegroup --sku B1 --is-linux
else 
    echo 'Error'
    exit 1
fi 

echo "Creating web app"
if [ $? -eq 0 ]; then 
    resource_id=$(az group show --resource-group $resourcegroup --query id --output tsv)
    az acr update -n $registry --admin-enabled true
    az webapp create --resource-group $resourcegroup --plan $appserviceplan --name $webappname -i "${registry}.azurecr.io/${container}:latest" --role acrpull --scope $resource_id --assign-identity '[system]'
else 
    echo 'Error'
    exit 1
fi 

if [ $? -eq 0 ]; then 
    echo "Done!"
    exit 0
else    
    echo 'Error'
    exit 1
fi