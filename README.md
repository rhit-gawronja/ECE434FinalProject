# ECE434 - Embedded Linux - FinalProject -  Rhian Seneviratne and Joey Gawron

## IOT Entry Way Camera

Using OpenCV, SMPT messaging, and FFmpeg we have successfully made a system that can monitor who is in a room. The BeaglePlay is set up to continually upload to a Twitch livestream with the camera feed using FFmpeg. During the script, every two minutes (customizable), a frame will be captured and will run through some image processing to be fed to the OpenCV HOG person detector. If a person is detected in the image, using SMPT, a message will be sent to the designated phone number that there may be an individual in the room. It will also email a picture of the room at the time a person was detected.

For a full breakdown of the project and instructions, please go to: https://elinux.org/ECE434_Project_-_IOT_Entry_Way_Camera 
