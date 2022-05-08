#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:27:36 2021

@author: dany98
"""

import qiskit
from qiskit import IBMQ
print(qiskit.__qiskit_version__)

token = '88940f04b59f4f36bcdcc889a671cd2e52b6b4ae0f7f10f9c111b2af90d533ac1b00b6c61de2e496587fe2f6d8eb5240a9073d47c91d74c80581682ac81acec6'

IBMQ.save_account(token)
IBMQ.load_account()
