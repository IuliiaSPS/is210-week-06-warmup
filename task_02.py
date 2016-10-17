#!usr/bin/env python
#! -*- coding: utf-8 -*-
"""Task_02"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

VAR1 = BALLETS [1]

BALLETS[1] = 'Swan' + VAR1[-5:]

BALLETS.append('Herman Schmerman')


BALLETS.extend(['Don Quixote', 'Sylvia'])
    
print BALLETS
