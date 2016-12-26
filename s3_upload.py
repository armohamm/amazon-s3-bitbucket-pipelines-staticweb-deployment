"""
A BitBucket Builds template for deploying an static website revision to AWS S3
chiusw2003@gmail.com
v1.0.0
"""
from __future__ import print_function
import os
import sys
import argparse
import boto3
from botocore.exceptions import ClientError


def getFiles(baseFolder):
  file_paths = []
  print(baseFolder)
  for root, directories, files in os.walk(baseFolder):
    for filename in files:
      filepath = os.path.join(root, filename)
      file_paths.append(filepath)
  return file_paths


def upload_to_s3(bucket_name, sourceDir):
  """
  Uploads an artefact to Amazon S3
  """
  try:
    client = boto3.client('s3')
    resource = boto3.resource('s3')
  except ClientError as err:
    print("Failed to create boto3 client.\n" + str(err))
    return False
  try:
    # clean the bucket
    bucket = resource.Bucket(bucket_name)
    for key in bucket.objects.all():
      key.delete()

    # upload the new files
    uploadFileNames = getFiles(sourceDir)
    print("Found " + len(uploadFileNames).__str__() + ' files')

    for filename in uploadFileNames:
      destName = os.path.join(*(filename.split('/')[1:]))
      print("Uploading file " + filename + ' to ' + destName)
      resource.Object(bucket_name, destName).put(Body=open(filename, 'rb'),
                                                 ContentType=get_contenttype_from_filename(filename))

  except ClientError as err:
    print("Failed to upload artefact to S3.\n" + str(err))
    return False
  except IOError as err:
    print("Failed to access artefact in this directory.\n" + str(err))
    return False

  return True


def get_contenttype_from_filename(filename):
  if filename.endswith(".js"):
    return 'application/x-javascript'
  elif filename.endswith(".js"):
    return 'text/css'
  elif filename.endswith(".html"):
    return 'text/html'
  else:
    return ''


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("bucket", help="Bucket name")
  parser.add_argument("sourceDir", help="Name of the directory to be uploaded to S3")
  args = parser.parse_args()

  if not upload_to_s3(args.bucket, args.sourceDir):
    sys.exit(1)


if __name__ == "__main__":
  main()
