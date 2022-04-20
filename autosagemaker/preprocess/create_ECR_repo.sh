#!/bin/bash  
# Bash script  
# Create ECR repository and push docker image

#  1            2              3          4                         5
# account_id, ecr_repository, region , processing_repository_uri , tag

echo "$2"
docker build -t $2 docker
$(aws ecr get-login --region $3 --registry-ids $1 --no-include-email)
aws ecr create-repository --repository-name $2
docker tag {$2 + $5} $4
docker push $4