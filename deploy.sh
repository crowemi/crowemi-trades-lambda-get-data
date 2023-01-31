REGION="us-west-2"
ECR_REGISTRY="926488920335.dkr.ecr.us-west-2.amazonaws.com"
ECR_REPOSITORY="crowemi-trades-lambda-get-data"
IMAGE_TAG="latest"

aws --profile=crowemi lambda wait function-exists --function-name crowemi-trades-lambda-get-data
if [ $? == 200 ]
then
    # re-deploy lambda
    aws --profile=crowemi lambda update-function-code --region us-west-2 --function-name "crowemi-trades-lambda-get-data" --image-uri "$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"
else
    # create lambda
    aws --profile=crowemi lambda create-function --function-name crowemi-trades-lambda-get-data --role arn:aws:iam::926488920335:role/crowemi-trades-lambda-get-data --code ImageUri="$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG" --package-type Image
fi