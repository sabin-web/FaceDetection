import boto3
import os
import json
import base64


# Change photo to the path and filename of your image. 

photo='/home/sabin/Desktop/LabAssignment-3/jayz.jpg'    

client=boto3.client('rekognition', region_name='us-west-2',aws_access_key_id='ASIAZYDC2QN5ZMQ3LQOK',aws_secret_access_key='NH+Wwi+kCaYAy1xvhBSZk3taXfBrslaQbmVoEft7')

with open(photo, 'rb') as image:

    response = client.recognize_celebrities(Image={'Bytes': image.read()})    

#print(response)

print('Detected faces for ' + photo)    

for celebrity in response['CelebrityFaces']:

    print ('Name: ' + celebrity['Name'])

    print ('Id: ' + celebrity['Id'])

    print ('Position:')

    print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))

    print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))

    print ('Info')

    for url in celebrity['Urls']:

        print ('   ' + url)