import boto3
import yaml
import subprocess

params = yaml.safe_load(open("../../params.yaml"))["autosagemaker"]["preprocess"]
ecr_repository = params["ecr_repository"]
region = params["region"]


account_id = boto3.client("sts").get_caller_identity().get("Account")
tag = ":latest"

uri_suffix = "amazonaws.com"
if region in ["cn-north-1", "cn-northwest-1"]:
    uri_suffix = "amazonaws.com.cn"
processing_repository_uri = "{}.dkr.ecr.{}.{}/{}".format(
    account_id, region, uri_suffix, ecr_repository + tag
)


#  1            2              3          4                         5
# account_id, ecr_repository, region , processing_repository_uri , tag

subprocess.Popen(['create_ECR_repo.sh %s %s %s %s %s' %(account_id,ecr_repository,region,processing_repository_uri,tag)], shell = True)

#subprocess.run([f"create_ECR_repo.sh {account_id} {ecr_repository} {region} {processing_repository_uri} {tag}"],shell=True)


