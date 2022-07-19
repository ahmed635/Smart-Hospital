# Smart-Hospital
## Introduction 
A remote smart healthcare system is proposed for monitoring patients’ health status and receiving doctors’ prescriptions by a workstation nurse in the hospital and medication nurse for supplying patient with the suitable medicine while patients staying at home. Besides this the Manager can also follow up the data analysis from data collected remotely from the patients and Medication nurse performance for specific management decisions. With the proposed system, patients can be remotely monitored from their homes, and can also live a more comfortable life through the use of some features of smart home and hospital healthcare system on their websites so that there are a lot of problems in hospitals such as the crowds during the pandemic, high infection, medical staff shortage, monitoring of chronic patients, and high cost.

## This project focuses on solving those problems through
-	Monitoring the patients from home and transferring vital signs of the patients to workstation of the hospital such as blood pressure, spo2, heart rate, and temperature.
-	Hospital will provide a medication nurse to give medicines to the patients. 
-	Workstation nurse for monitoring patients and will contact a doctor if any abnormalities occur and send an ambulance to home of the patient.

## Motivation
- The primary role of any remote smart hospital system is to assist users in remotely controlling and monitoring with enables a comfortable and convenient lifestyle. With this in mind, we are motivated to provide a wide healthcare service to reduce the number of deaths caused by the crowd of hospitals as our project aims to help the doctors monitoring patients remotely from home. The proposed system monitors and records vital signs in a module, sends recorded parameters to the doctor by workstation nurse and controls the patients as well. 
- The second motivation that We want to reduce the cost of healthcare services for the patients and also increase the income of healthcare providers by offering services that has low operating cost. 
- The third motivation that we want to solve the problem of medical staff shortage by increasing the quality of healthcare with the remote smart hospital monitoring.

## Block Diagram

![Screenshot 2022-07-19 131736](https://user-images.githubusercontent.com/58488520/179740474-eb273ebf-0c1d-421d-8bd2-8c689468b790.jpg)

## Hardware Devices
### 1. Pulse oximeter
It is based on max30101 pulse oximeter sensor that is an integrated pulse oximetry and heartrate monitor module. It includes internal LEDs(red, green and IR) photodetectors, optical elements, and low-noise electronics.it measures the heart rate by analyzing the time series response of the reflected light , measures the spo2 by the magnitude of the returned light. The sensor is connected to the microcontroller (esp32) by using i2c connection then the values are displayed onthe oled of the pulse oximeter and on the website.

![Screenshot 2022-07-19 134242](https://user-images.githubusercontent.com/58488520/179742218-ea79b4e5-afc2-4b4f-9c1d-59b262b65e5a.jpg)

### 2. Blood pressure monitor
As we know the blood pressure signal is a noisy signal so we found it is better to use a medical device and implement it in our system. We used a Bluetooth digital blood pressure monitor device then we uses a Bluetooth low energy protocol to make a connection between the blood pressure device and the microcontroller (esp32) so the readings of the device are transferred to the microcontroller.

![Screenshot 2022-07-19 141042](https://user-images.githubusercontent.com/58488520/179747276-2b18c289-55a1-4884-b35d-42de70bdd1df.jpg)
![Screenshot 2022-07-19 141127](https://user-images.githubusercontent.com/58488520/179747284-ee344cb2-c678-4c51-aa2d-f76e9e47ae5f.jpg)

### 3. Thermal gun
It is based on GY-906 MLX90614 BCC Contactless Infrared Temperature Sensor that uses non-contact temperature sensing to collect temperature information without touching any specific surface. Although invisible to the human eye, all objects emit infrared light, and the concentration varies with temperature. The sensor is connected to the microcontroller (esp32) by using i2c connection then the values are displayed When you press the on-off switch then the device will be powered on then when you hold on the momentary switch then the laser and the sensor will be turned on and the oled will show the readings.

![Screenshot 2022-07-19 140948](https://user-images.githubusercontent.com/58488520/179747321-9f1bf76e-73d7-4f8c-be01-21a832c088b5.jpg)
