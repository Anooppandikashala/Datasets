## Pycharm Installation

1. Goto Pycharm [Download](https://www.jetbrains.com/pycharm/download/#section=linux) Section 
2. Accept the terms and conditions and Download the file.
3. Goto Download folder 
4. Extract the tar.gz file by (right click the file and Extract here)
5. Then open the extracted folder and go to ``` bin ``` folder
6. Inside the folder open the terminal (right click and open terminal)
7. To install the pycharm ide type
```
 ./pycharm.sh
```
8. It will open the installation window And go through the instructions.




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

sudo pip install keras==2.1.3
```

4. Opencv installation in Ubuntu
```
sudo pip install opencv-python
```




