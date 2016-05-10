# Upload to Amazon S3
An example repository to demonstrate the Amazon S3 upload for Bitbucket pipelines addon. This example uploads an artefact to an existing S3 bucket. 


## How To Use It
* Create a S3 bucket to hold the artefact(s)
* Add/Modify the required Environment Variables below

## Required Permissions in AWS
It is recommended you [create](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) a separate user account used for this deploy process.  This user should be associated with a group that has the `AmazonS3FullAccess` [AWS managed policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) attached for the required permissions to upload a new artefact to the S3 bucket.

Note that the above permissions are more than what is required in a real scenario. For any real use, you should limit the access to just the S3 bucket in your context.

## Required Environment Variables
* `AWS_SECRET_ACCESS_KEY`:  Secret key for a user with the required permissions.
* `AWS_ACCESS_KEY_ID`:  Access key for a user with the required permissions.
* `AWS_DEFAULT_REGION`:  Region where the target Elastic Beanstalk application is.
* `S3_BUCKET_NAME`: Name of target S3 bucket.
* `ARTEFACT_NAME`: Name of the artefact to be uploaded.


# License
Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Note: Other license terms may apply to certain, identified software files contained within or distributed with the accompanying software if such terms are included in the directory containing the accompanying software. Such other license terms will then apply in lieu of the terms of the software license above.
