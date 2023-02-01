# crowemi-trades-lambda-get-data
This repository stores code for retreiving data from [Polygon](https://polygon.io/) API and storing it on S3 for future analysis.

## Environment Variables
`BUCKET`: the bucket where the lambda should drop files.

`POLYGON_KEY`: the Polygon API key.

`polygon_key` (deprecated): the Polygon API key.

`AWS_ACCESS_KEY_ID`: the AWS access key for accessing AWS resources.

`AWS_SECRET_ACCESS_KEY`: he AWS secret access key for accessing AWS resources.

`ECR_REGISTRY`: the ECR registry where the lamba images is stored.

`ECR_REPOSITORY`: the ECR repository where the lambda image is stored.

`IMAGE_TAG`: the image tag to deploy.