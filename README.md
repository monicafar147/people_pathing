# people_pathing
Using AWS rekognition to track people in a queue

to run the code:
- clone the repository to an empty folder
- run the following in a terminal in the cloned repository
```python demo_rekognition.py```
- to save the output in a .txt file
```python demo_rekognition.py > temp.txt```

if you want to analyse another video
1. add that video to a s3 bucket
2. specify the bucket name and video name in demo_rekognition.py in the main function
3. run ```python demo_rekognition.py```
