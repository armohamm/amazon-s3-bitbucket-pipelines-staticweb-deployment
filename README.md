# Upload to Amazon S3
An example script and configuration for uploading to an existing [Amazon S3](https://aws.amazon.com/s3/) bucket with BitBucket Pipelines.  This repository also includes a sample artefact to be uploaded as a demo.

## How To Use It
* [Create an S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) to hold the artefact(s).
* Add the required Environment Variables below in Build settings of your Bitbucket repository.
* Copy `s3_upload.py` to your project.
* Copy `bitbucket-pipelines.yml` to your project.
  * Or use your own, just be sure to include all steps in the sample yml file.
* Copy `SampleApp_Linux.zip` to your project if you would like to use a sample artefact.

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

# License
Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Note: Other license terms may apply to certain, identified software files contained within or distributed with the accompanying software if such terms are included in the directory containing the accompanying software. Such other license terms will then apply in lieu of the terms of the software license above.
