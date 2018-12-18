# ECEN 689 Project 2
---

Obstacles' detection through a Stereoscopic cameras' setup. Utilizing OpenCV, and written in Python.
We're using our own generated data.

---

### Team members:

1) Drupad Khublani
2) Michael Bass
3) Khaled Nakhleh
4) Venkata Pydimarri

---

### Custom-built rover (built by Michael Bass)

![alt text](https://github.com/khalednakhleh/ECEN689Project2/blob/master/assets/image.jpeg "Rover - top view")

![alt text](https://github.com/khalednakhleh/ECEN689Project2/blob/master/assets/image_2.jpeg "Rover - front view")

### Stitched images' runs below
---
### First run
Batch size: 35
No. epochs: 5
optimizer: adam
shear range = 0.3
zoom range = 0.25
Validation split: 0.05
3 Convolutional layers
Data across runs:
* Epoch 1
loss: 7.4802   accuracy: 0.5255   Validation loss: 7.9439   Validation accuracy: 0.5071
* Epoch 2
loss: 7.6328   accuracy: 0.5264   Validation loss: 7.3264   Validation accuracy: 0.5455
* Epoch 3
loss: 7.5862   accuracy: 0.5293   Validation loss: 7.9924   Validation accuracy: 0.5041
* Epoch 4
loss: 7.6177   accuracy: 0.5274   Validation loss: 7.3264   Validation accuracy: 0.5455
* Epoch 5
loss: 7.6547   accuracy: 0.5251   Validation loss: 7.5928   Validation accuracy: 0.5289

--- 
### Second run
Batch size: 20
No. epochs: 10
optimizer: adam
shear range = 0.2
zoom range = 0.2
Validation split: 0.025
4 Convolutional layers
Accuracy rate across runs:
* Epoch 1
loss: 0.5680   accuracy: 0.6664   Validation loss: 0.2504   Validation accuracy: 0.9167
* Epoch 2
loss: 0.1840   accuracy: 0.9286   Validation loss: 0.0912   Validation accuracy: 0.9655
* Epoch 3
loss: 0.0817   accuracy: 0.9714   Validation loss: 0.0077   Validation accuracy: 1.0000
* Epoch 4
loss: 0.0687   accuracy: 0.9753   Validation loss: 0.0675   Validation accuracy: 0.9828
* Epoch 5
loss: 0.0483   accuracy: 0.9806   Validation loss: 0.0096   Validation accuracy: 1.0000
* Epoch 6
loss: 0.0589   accuracy: 0.9785   Validation loss: 0.0149   Validation accuracy: 1.0000
* Epoch 7
loss: 0.0395   accuracy: 0.9862   Validation loss: 0.0015   Validation accuracy: 1.0000
* Epoch 8
loss: 0.0265   accuracy: 0.9911   Validation loss: 0.0055   Validation accuracy: 1.0000
* Epoch 9
loss: 0.0323   accuracy: 0.9875   Validation loss: 0.0230   Validation accuracy: 1.0000
* Epoch 10
loss: 0.0321   accuracy: 0.9907   Validation loss: 0.0053   Validation accuracy: 1.0000

---
### Third run
Batch size: 50
No. epochs: 10
optimizer: adam
shear range = 0.1
zoom range = 0.1
Validation split: 0.025
5 Convolutional layers
Data across runs:
* Epoch 1
loss: 0.6772   accuracy: 0.5563   Validation loss: 0.4467   Validation accuracy: 0.8800
* Epoch 2
loss: 0.2563   accuracy: 0.8814   Validation loss: 0.0686   Validation accuracy: 1.0000
* Epoch 3
loss: 0.0924   accuracy: 0.9679   Validation loss: 0.0018   Validation accuracy: 1.0000
* Epoch 4
loss: 0.0538   accuracy: 0.9819   Validation loss: 3.29x10^-6   Validation accuracy: 1.0000
* Epoch 5
loss: 0.0345   accuracy: 0.9883   Validation loss: 0.0016   Validation accuracy: 1.0000
* Epoch 6
loss: 0.0448   accuracy: 0.9850   Validation loss: 0.0043   Validation accuracy: 1.0000
* Epoch 7
loss: 0.0271   accuracy: 0.9896   Validation loss: 0.0021   Validation accuracy: 1.0000
* Epoch 8
loss: 0.0264   accuracy: 0.9913   Validation loss: 2.59*10^-4   Validation accuracy: 1.0000
* Epoch 9
loss: 0.0176   accuracy: 0.9940   Validation loss: 7.24*10^-5   Validation accuracy: 1.0000
* Epoch 10
loss: 0.0220   accuracy: 0.9940   Validation loss: 5.58*10^-6   Validation accuracy: 1.0000

---
### Fourth run
Batch size: 15
No. epochs: 10
optimizer: adam
shear range = 0.05
zoom range = 0.05
Validation split: 0.025
5 Convolutional layers
Data across runs:
* Epoch 1
loss: 0.6940   accuracy: 0.5258   Validation loss: 0.6923   Validation accuracy: 0.5200
* Epoch 2
loss: 0.6028   accuracy: 0.6394   Validation loss: 0.4332   Validation accuracy: 0.6984
* Epoch 3
loss: 0.1697   accuracy: 0.9333   Validation loss: 0.1307   Validation accuracy: 0.9365
* Epoch 4
loss: 0.0657   accuracy: 0.9767   Validation loss: 0.2508   Validation accuracy: 0.9683
* Epoch 5
loss: 0.0581   accuracy: 0.9787   Validation loss: 0.0073   Validation accuracy: 1.0000
* Epoch 6
loss: 0.0499   accuracy: 0.9839   Validation loss: 0.0027   Validation accuracy: 1.0000
* Epoch 7
loss: 0.0365   accuracy: 0.9869   Validation loss: 0.0041   Validation accuracy: 1.0000
* Epoch 8
loss: 0.0223   accuracy: 0.9905   Validation loss: 2.05x10^-4   Validation accuracy: 1.0000
* Epoch 9
loss: 0.0331   accuracy: 0.9888   Validation loss: 0.0076   Validation accuracy: 1.0000
* Epoch 10
loss: 0.0154   accuracy: 0.9947   Validation loss: 3.68x10^-5   Validation accuracy: 1.0000

---
### Fifth run
Batch size: 10
No. epochs: 15
optimizer: adam
shear range = 0.01
zoom range = 0.01
Validation split: 0.025
5 Convolutional layers
Data across runs:

* Epoch 1
loss: 0.6422   accuracy: 0.5819   Validation loss: 0.3604   Validation accuracy: 0.8267
* Epoch 2
loss: 0.2240   accuracy: 0.9080   Validation loss: 0.2960   Validation accuracy: 0.9048
* Epoch 3
loss: 0.1112   accuracy: 0.9609   Validation loss: 0.0213   Validation accuracy: 1.0000
* Epoch 4
loss: 0.0484   accuracy: 0.9855   Validation loss: 0.0098   Validation accuracy: 1.0000
* Epoch 5
loss: 0.0351   accuracy: 0.9875   Validation loss: 0.0160   Validation accuracy: 0.9841
* Epoch 6
loss: 0.0281   accuracy: 0.9895   Validation loss: 0.0046   Validation accuracy: 1.0000
* Epoch 7
loss: 0.0331   accuracy: 0.9908   Validation loss: 2.00x10^-4   Validation accuracy: 1.0000
* Epoch 8
loss: 0.0210   accuracy: 0.9941   Validation loss: 3.36x10^-4   Validation accuracy: 1.0000
* Epoch 9
loss: 0.0309   accuracy: 0.9921   Validation loss: 0.0157   Validation accuracy: 0.9841
* Epoch 10
loss: 0.0078   accuracy: 0.9967   Validation loss: 0.0031   Validation accuracy: 1.0000
* Epoch 11
loss: 0.0159   accuracy: 0.9954   Validation loss: 1.47x10^-7   Validation accuracy: 1.0000
* Epoch 12
loss: 0.0435   accuracy: 0.9859   Validation loss: 0.0024   Validation accuracy: 1.0000
* Epoch 13
loss: 0.0097   accuracy: 0.9964   Validation loss: 1.32x10^-6   Validation accuracy: 1.0000
* Epoch 14
loss: 0.0059   accuracy: 0.9977   Validation loss: 1.34x10^-4   Validation accuracy: 1.0000
* Epoch 15
loss: 0.0059   accuracy: 0.9764   Validation loss: 0.3492   Validation accuracy: 0.8571

