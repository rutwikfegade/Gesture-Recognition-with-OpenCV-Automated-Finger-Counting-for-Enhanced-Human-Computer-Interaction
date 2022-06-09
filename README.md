## Counting-finger-using-opencv
The Opencv library is used in conjunction with Python to detect the hand and count the fingers.
It just counts from 0 to 5 the number of fingers in front of the camera.
The hand's terminal points form a complete shape.
This contour indicates that a hand has been identified.
When the palm is open, we count the number of gaps between the fingers to determine the number of fingers.
This void forms a defect in the contour, which we can count to get the number of fingers.
So there are four defects, or gaps, for each of the five fingers.

![0](https://user-images.githubusercontent.com/69248756/172680548-f62590e2-c9a1-4358-8efb-64549376b5a3.PNG)


![1](https://user-images.githubusercontent.com/69248756/172680576-95bcf1ec-f3e4-48e1-9940-6340a0172e33.PNG)


![2](https://user-images.githubusercontent.com/69248756/172680582-08a137df-cd38-47dc-882b-aa6169868b70.PNG)


![3](https://user-images.githubusercontent.com/69248756/172680591-cd42df42-e614-42b3-911e-2655249b3315.PNG)


![4](https://user-images.githubusercontent.com/69248756/172680602-8e19184d-a808-47a8-98a6-0a7529157db4.PNG)


![5](https://user-images.githubusercontent.com/69248756/172680631-93866312-af42-4058-9e65-79261d3f9a2a.PNG)


The blue dot seen are the defects found.


### Led on/off using 1/0



https://user-images.githubusercontent.com/69248756/172681495-48c206e2-958d-4f2e-8ce2-16f535fdb18d.mp4

