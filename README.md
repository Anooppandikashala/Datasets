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




