import boto3 

def hello_world():
    print("Hello world!")

#function assumes valid AWS creds
def get_s3_bucket(name=None):
    if name is None:
        # Retrieve the list of existing buckets
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        # Output the bucket names
        print("No bucket name provided, listing available buckets.")
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    else:
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket(name)
        print(f"You selected bucket {name}, below is the content of this bucket:")
        for file in my_bucket.objects.all():
            print(file.key)
    
if __name__ == "__main__":
    # execute only if run as a script from somewhere else
    hello_world()
    get_s3_bucket()
    get_s3_bucket(name="My_Bucket123")
