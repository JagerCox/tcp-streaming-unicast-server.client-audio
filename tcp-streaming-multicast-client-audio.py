#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import pyaudio

"""
    File name: tcp-streaming-unicast-client-audio.py
    Author: Jäger Cox // jagercox@gmail.com
    Date created: 05/08/2016
    License: MIT
    Python Version: 2.7
    Code guide line: PEP8
"""

__author__ = "Jäger Cox // jagercox@gmail.com"
__created__ = "05/08/2016"
__license__ = "MIT"
__version__ = "0.1"
__python_version__ = "2.7"
__email__ = "jagercox@gmail.com"

# Pyaudio Initialization
CHUNK = 1024
CHANNELS = 1
RATE = 10240
INPUT = True
FORMAT = pyaudio.paInt16

# Socket Initialization
HOST = '0.0.0.0'
PORT = 953
SIZE = 1024

if __name__ == '__main__':
    '''PyAudio initialization'''
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=INPUT,
                    frames_per_buffer=CHUNK)

    '''Socket server initialization'''
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((HOST, PORT))

    while True:
        data = stream.read(CHUNK)
        connection.send(data)
        connection.recv(SIZE)

    connection.close()
    stream.close()
    p.terminate()
