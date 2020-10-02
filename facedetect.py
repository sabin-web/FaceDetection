import boto3

import json



# Change photo to the path and filename of your image. 

photo='/home/sabin/Desktop/LabAssignment-3/jayz.jpg'
client=boto3.client('rekognition')

with open(photo, 'rb') as image:
	response_celeb = client.recognize_celebrities(Image={'Bytes': image.read()})
with open(photo,'rb') as image:
    response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])    

#print(response)

print('Detected faces for ' + photo)    

for celebrity in response_celeb['CelebrityFaces']:
    print ('Name: ' + celebrity['Name'])
    print('====================================')

for person in response['FaceDetails']:
    print(person['Emotions'])
    print('Gender:',person['Gender']['Value'])
    print('========================================')
    print('Age Range:'+str(person['AgeRange']['Low'])+'-'+str(person['AgeRange']['High']))
    print('========================================')
    print('Emotion:'+str(person['Emotions'][0]['Type']))
    print('Happy Percentage:'+str(person['Emotions'][0]['Confidence']))
    print("==========================================")
    print('Emotion:'+str(person['Emotions'][1]['Type']))
    print('Calm Percentage:'+str(person['Emotions'][1]['Confidence']))
    print('=========================================')
    print('Emotion:'+str(person['Emotions'][5]['Type']))
    print('Surprised Percentage:'+str(person['Emotions'][5]['Confidence']))
    print('=========================================')
    print('Emotion:'+str(person['Emotions'][6]['Type']))
    print('Angry Percentage:'+str(person['Emotions'][6]['Confidence']))
    print("===========================================")
    if person['Sunglasses']['Value']:
        print('Wearing Sunglasses ','\tConfidence:',person['Sunglasses']['Confidence'])
    if person['MouthOpen']['Value']:
        print('Mouth is open','\tConfidence:',person['MouthOpen']['Confidence'])
    if person['Eyeglasses']['Value']:
        print('Wearing Eyeglasses','\tConfidence:',person['Eyeglasses']['Confidence'])
    if person['Mustache']['Value']:
        print('Has a Moustache','\tConfidence:',person['Mustache']['Confidence'])
    # for face in response['FaceDetails']:
    #     emo = prettytable.PrettyTable(["Emotions", "Confidence"])
    #     for emotion in face['Emotions']:
    #         emo.add_row([emotion['Type'],'{:.3f}'.format(emotion['Confidence'])])
    # print(emo)