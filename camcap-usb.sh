#!/bin/bash
NOW=$(date +"%H-%M")
 echo $NOW
fileName="image"$NOW".jpg"
 echo $fileName
fswebcam  $fileName

