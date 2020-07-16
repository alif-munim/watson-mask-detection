# IBM-Hackathon-Mask-Barrier-Detection
## Problem Addressed
Employees are required to work with a mask on in Canada and additionally - most establishments are requiring patrons to wear masks when entering. To make sure all individuals have a mask on, an employee checks the individual upon entering the store. This practice puts the employee on the frontline and serves as a cause for the spread of COVID-19. When a customer comes up who is not wearing a mask the employee is at risk as they cannot control another person's actions if they get closer than 6 feet. Mask On seeks to help reduce this critical point of contact while also making sure incoming individuals are wearing masks.

## Solution Built
Mask On uses IBM Watson Studio’s Visual Recognition which will then activate the entrance gate if a mask is detected. An individual approaches the camera and presses a button to take a picture and automatically detect a mask. Upon verification of a mask on the individuals face the Jetsen controls a motor which lifts a barrier.  If the system is unable to verify a face mask, the barrier remains closed.  

## Problem Solved / Better than other solutions
The solution is tailored to businesses that put the safety of their employees first. Through the use of automatic face mask detection and the lifting of a barrier when a mask is present, our solution ensures any individual walking into the establishment is masked allowing the workers to perform their job. By reducing the number of people that come in contact, Mask On can reduce the spread of COVID-19. Backed by IBM Cloud Mask On is an affordable way of making sure people are wearing masks.

## Technology Used
IBM Watson Studio’s Visual Recognition processes each photo coming from the Jetson Nano hooked to a camera and a servo motor. The embedded device is running a Python program making API calls to IBM Cloud upon face detection. The servo motor activates, opening the gate only when a mask is detected at 85% confidence or higher.

## Next Steps
Currently the implementation on the Jetsen Nano makes a call to an external API - as this project is expanded on we would like to see the model be completely on the Jetsen having it operate independently of any external servers.
We would see this product scaling into on-board temperature readers that if a fever is detected does not allow the user to enter.  

### References
https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
