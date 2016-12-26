# Deploy static websites to Amazon S3
An example script and configuration for deploying static website to an existing [Amazon S3]
(https://aws.amazon.com/s3/) bucket with BitBucket Pipelines.  This repository also includes a
sample website to be uploaded as a demo.

## How To Use It
* [Create an S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) to
hold the static website.
* Add the required Environment Variables below in Build settings of your Bitbucket repository.
* Copy `s3_upload.py` to your project.
* Copy `bitbucket-pipelines.yml` to your project.
    * Or use your own, just be sure to include all steps in the sample yml file.
* Copy `dist` folder to your project if you would like to use a sample empty website.
* You will also need to [setup your AWS bucket](http://docs.aws.amazon
.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html) properly for static website hosting.
Make sure you have also [setup correct permission](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html) for publiclu accessible website.

## Required Permissions in AWS
It is recommended you [create](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) a separate user account used for this deploy process.  This user should be associated with a group that has the `AmazonS3FullAccess` [AWS managed policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) attached for the required permissions to upload a new artefact to the S3 bucket.

Note that the above permissions are more than what is required in a real scenario. For any real use, you should limit the access to just the AWS resources in your context.

## Required Environment Variables
* `AWS_SECRET_ACCESS_KEY`:  Secret key for a user with the required permissions.
* `AWS_ACCESS_KEY_ID`:  Access key for a user with the required permissions.

## Other things to consider
* You would ideally create/bundle your artefact as a build step before invoking the s3_upload python script.
* If you are likely to upload multiple versions of the artefact iteratively, you might want to consider enabling [S3 bucket versioning](http://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html).
* Uploading artefacts to S3 could be used in several contexts, like in conjunction with the other Bitbucket Pipelines integrations.
  * You could upload an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template, or an AWS [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) application.
  * Uploading to S3 could act as an input to the Source stage of an [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and trigger the pipeline.

## Acknowledgement
This repo is forked from official bitbucket pipelines support script from Amazon. [Original
Repository](https://bitbucket.org/awslabs/amazon-s3-bitbucket-pipelines-python). Also inspired by
 Marco Muscat's tutorial at his [personal website](http://www.lambdatwist.com/s3-hosting-guide/).
