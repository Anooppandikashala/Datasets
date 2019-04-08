# TransferLearning (Bottle type Recognition)

## Install wifi driver
```
sudo apt-get install git-core

```
```
sudo apt-get install git build-essential dkms
```

```
git clone -b extended --single-branch https://github.com/lwfinger/rtlwifi_new.git

```
```
cd rtlwifi_new

```
```
sudo dkms add ../rtlwifi_new
```
```
sudo dkms build rtlwifi-new/0.6 
```
```
sudo dkms install rtlwifi-new/0.6
```
```
sudo modprobe -v rtl8723de ant_sel=2 or sudo modprobe -v rtl8723be ant_sel=2
```

## Needed Packages and Installation of Python

1. Python and Pip
```
sudo apt update

# installing python 2.7 and pip for it
sudo apt install python2.7 python-pip

```
2. PyQt4 and PyQt-Designer
```
sudo apt-get install python-qt4 qt4-designer

```
3. Tensorflow and Keras
```
sudo pip install tensorflow==1.7.0

sudo pip install keras-2.1.3
```



1. Dowload the codes and save to any folder ```folder_name```
2. create a  ```model``` folder in your ```folder_name```
3. The trained model(folder) can be dowloaded from [here](https://drive.google.com/open?id=1Q7LVvaZqOvrpFDzEWW5g7e1wGmLKVpXU)(Old Trained Models with 94% accuracy)
4. Dowload the model folder.
5. And copy the ```model_weights.h5``` to ```folder_name/model``` and run the ```Home.py```

## Opencv installation in Ubuntu
```
sudo pip install opencv-python
```
## Updated data-set
You can download updated data-set from my Dataset Repo [https://github.com/Anooppandikashala/Datasets](https://github.com/Anooppandikashala/Datasets)

## Real time Bottle Recognition Using Opencv
1. Clone or download the Repo
2. Download latest trained ```model``` from [here](https://drive.google.com/open?id=14n_vhGU17c4B3Azc1mnMCr75ffxP7B2z)(98% Accuracy)
3. Download ```model_weights.h5```  and  ```model.json``` and save to ```model```  folder.
4. run ```Home.py ``` and click ```From Camera``` 
5. It open a new window and show a camera window.
6. A blue Square can be seen in camera window.
7. you can place any bottle infront of camera and adjust to the blue square, it will recognize the bottle type.

### Latest Trained Model
You can download from [here](https://drive.google.com/open?id=14n_vhGU17c4B3Azc1mnMCr75ffxP7B2z)(98% Accuracy)

### Screenshots

![Screenshot1](https://github.com/Anooppandikashala/TransferLearning/blob/master/ScreenShots/Screenshot%20from%202019-04-07%2023-28-291.png)

## Admin Login

Added a simple Admin Module. You can implement using Sqlite or other methods.

Here admin username : ```admin```
     admin password : ```admin123```
