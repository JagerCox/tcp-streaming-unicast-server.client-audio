#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import pyaudio

"""
    File name: tcp-streaming-unicast-server-audio.py
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

# PyAudio configuration
CHUNK = 1024
CHANNELS = 1
RATE = 10240
OUTPUT = True
FORMAT = pyaudio.paInt16

# Server configuration
HOST = '0.0.0.0'
PORT = 953
BACKLOG = 5
SIZE = 1024

if __name__ == '__main__':
    '''PyAudio initialization'''
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=OUTPUT)

    '''Socket server initialization'''
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((HOST, PORT))
    connection.listen(BACKLOG)

    server, address = connection.accept()

    while True:
        data = server.recv(SIZE)
        if data:
            stream.write(data)  # Stream to send
            # client.send('ACK')  # Not necessary

    server.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
