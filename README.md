# REC2000

This is a small python software which transfers data from **Zeiss Elta** total stations to a computer via serial to USB adapter cable.

## Zeiss Elta

The Zeiss **Elta** (**El**ektronisches **Ta**chymeter) total stations were produced by Zeiss Jena in Germany in the 1990ies. Old stocks are still available around Germany and are sold at reasonable prices. 

**Zeiss Elta 14 T:**

<img src="https://user-images.githubusercontent.com/21182528/43457628-c24ef85a-94c7-11e8-8437-6579f97467b9.jpg" width="600">
<img src="https://user-images.githubusercontent.com/21182528/43457631-c29458aa-94c7-11e8-9215-6e89003002eb.jpg" width="600">

Essentially, two different types were produced:
* REC Elta 13, 14, 15
* Elta 13, 14, 15

The diffenrence is that the "REC" types were able to store data in the device, whereas the types without "REC" could only spend data on the fly via serial port.
Using this software, you are able to transfer data from the total station via serial port, using a serial/USB adapter to any PC.

<img src="https://user-images.githubusercontent.com/21182528/43457630-c2737a54-94c7-11e8-88a5-0b3ea92c1d0a.jpg" width="600">
<img src="https://user-images.githubusercontent.com/21182528/43457633-c2cf9852-94c7-11e8-8f5d-4bac579b5ec2.jpg" width="600">

The software requests you to start the measurement at the total station. The results are displayed on the totals stations screen and are instantly transferred via serial port to the PC. The python script shows the transferred data and stores it sequentially in a file named "daten.txt".

<img src="https://user-images.githubusercontent.com/21182528/43457794-47bc672a-94c8-11e8-826f-2f7dfe7a440a.jpg" width="600">
