# Bash script to initiate and run the 'basicPubSub.py' application provided by AWS-IOT-DEVICE-SDK.
# Custom end point specified by -e option corresponds to the AWS IOT thing.
# -m publish option runs the basicPubSub.py application in 'publish' mode, i.e. publishing to topic sdk/test/Python

# Running the script: issue the command -- ./start.sh from a Bash shell

# Author: AWS
# Modified: Shiril Tichkule, Jeet Baru
# Date: 11 November 2018

# stop script on error
set -e

# Check to see if root CA file exists, download if not
if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from AWS...\n"
  curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt
fi

# install AWS Device SDK for Python if not already installed
if [ ! -d ./aws-iot-device-sdk-python ]; then
  printf "\nInstalling AWS SDK...\n"
  git clone https://github.com/aws/aws-iot-device-sdk-python.git
  pushd aws-iot-device-sdk-python
  python setup.py install
  popd
fi

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python aws-iot-device-sdk-python/samples/basicPubSub/basicPubSub.py -e your_thing.us-west-2.amazonaws.com -r root-CA.crt -c RPi3.cert.pem -k RPi3.private.key -m publish
