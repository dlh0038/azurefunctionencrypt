import logging
import boto3
import os
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # with open("/home/user/Documents/azurefunction/public.pem", 'rb') as key_file:
    #     public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
    public_key = serialization.load_pem_public_key(os.getenv('rsa_public_key').encode('utf-8'), backend=default_backend())
    #logging.info(f"public key {public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)}")

    try:
        req_body = req.get_json()
        name = req_body.get('name')
        if name:
            ciphertext = public_key.encrypt(bytes(name, 'utf-8'), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
            logging.info(f"Cipher: {ciphertext}")
            s3_client = boto3.client('s3',
                                     region_name=os.getenv('regionname'),
                                     aws_access_key_id=os.getenv('awskeyid'),
                                     aws_secret_access_key=os.getenv('awssecret'))

            s3_client.put_object(Bucket=os.getenv('awsbucket'), 
                                 Key=f"test_encrypt{datetime.datetime.now().strftime('%m%d%Y%H%M%S')}.txt", 
                                 Body=ciphertext, 
                                 ServerSideEncryption='aws:kms')
            logging.info("sent to s3 bucket")
            return func.HttpResponse(f"This HTTP triggered function executed successfully.")
    except ValueError:
        pass

        

    
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
