/*
Node JS routine for reading and displaying temperature and humidity measurements
collected using a DHT22 sensor connected to the Raspberry Pi 3. 10 data points are read in
(once every 10 seconds), and after the 100 seconds of reading time elapse, the
minumum, maximum, and average values of temperature and humidity recorded are displayed.

Author: Shiril Tichkule
Date: 5 October 2018

Node version: v8.12.0

References:
https://www.losant.com/blog/how-to-install-nodejs-on-raspberry-pi
https://github.com/momenso/node-dht-sensor
https://www.airspayce.com/mikem/bcm2835/
https://www.npmjs.com/package/rpi-dht-sensor
*/

var sensorLib = require('node-dht-sensor'); //requirement of the node-dht-sensor library to be installed
var i=0; //counter variable
var temp_arr = []; //arrays to store temp and rh values
var rh_arr = [];
var temp_max = -40.0; //initial values based on DHT22 datasheet
var temp_min = 125.0;
var temp_sum = 0.0;
var temp_avg = 0.0;
var rh_max = 0.0;
var rh_min = 100.0;
var rh_sum = 0.0;
var rh_avg = 0.0;

var dht_sensor = {
    initialize: function () { //function to initialize DHT22 connected to GPIO4
        return sensorLib.initialize(22, 4);
    },
    read: function () { //function to read temp and rh values from DHT22
        var readout = sensorLib.read();
        console.log('Temperature: ' + readout.temperature.toFixed(1) + ' °C, ' +
            'Humidity: ' + readout.humidity.toFixed(1) + ' %'); //display floats with 1 digit after decimal point
        temp_arr.push(readout.temperature.toFixed(1)); //append values to arrays
        rh_arr.push(readout.humidity.toFixed(1));
        i++;
        if(i<10){ //repeat at 10 second intervals until 10 measurements are done
        setTimeout(function () {
            dht_sensor.read();
        }, 10000);
        }
        else dht_sensor.analyze(); //else compute and display statistics
    },
    analyze: function () { //function to analyze recorded data
        console.log('\nMeasurements completed...now showing statistics:\n');
        for(i=0;i<10;i++){
            if(temp_arr[i]>temp_max) temp_max = temp_arr[i]; //max and min of temp
            if(temp_arr[i]<temp_min) temp_min = temp_arr[i];
            if(rh_arr[i]>rh_max) rh_max = rh_arr[i]; //max and min of rh
            if(rh_arr[i]<rh_min) rh_min = rh_arr[i];
            temp_sum += parseFloat(temp_arr[i]);
            rh_sum += parseFloat(rh_arr[i]);
            }
        temp_avg = temp_sum/10.0; //average temp and rh values
        rh_avg = rh_sum/10.0;
        /* Print statistics */
        console.log('Lowest Temperature: ' + temp_min + ' °C');
        console.log('Lowest Humidity: ' + rh_min + ' %');
        console.log('Highest Temperature: ' + temp_max + ' °C');
        console.log('Highest Humidity: ' + rh_max + ' %');
        console.log('Average Temperature: ' + temp_avg.toFixed(1) + ' °C');
        console.log('Average Humidity: ' + rh_avg.toFixed(1) + ' %');
    }
};

if (dht_sensor.initialize()) { //if sensor is initialized successfully, read data
   dht_sensor.read();
} else { //else print warning message to console
    console.warn('Failed to initialize sensor');
}