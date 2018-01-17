#!/usr/bin/python

# Copyright 2017 Sam Strachan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Hardware: https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi
# Reference: http://gpiozero.readthedocs.io/en/stable/source_values.html

from gpiozero import LEDBoard
from gpiozero.tools import random_values

from signal import pause
from time import sleep

class Tree( object ):
    Lower = 2
    Upper = 28

    Period = 20

    def __init__( self ):
        self.tree = LEDBoard(
            *range( Tree.Lower, Tree.Upper ),
            pwm=True)

    def reset( self ):
        for led in self.tree:
            led.source_delay = 0
            led.source = [ 0 ]

    def off( self ):
        self.tree.off()

    def on( self ):
        self.tree.on()

    def pulse( self ):
        self.tree.pulse(
            fade_in_time = 4,
            fade_out_time = 4 )

    def flicker( self ):
        for led in self.tree:
            led.source_delay = 0.2
            led.source = random_values()

    def sequence( self ):
        delay = Tree.Period * 1.0 / ( Tree.Upper - Tree.Lower )
        values = []
        for index in range( Tree.Lower, Tree.Upper ):
            values.append( 0 )

        index = 0
        for led in self.tree:
            #delay += 0.1
            led.source_delay = delay
            values[index] = 1
            led.source = list( values )
            values[index] = 0
            index += 1
            #print( led.source )
            #led.on()
            #sleep( 0.1 )
            #led.off()

    def wait( self ):
        sleep( Tree.Period )

    def go( self ):
        while True:
            self.sequence()
            self.wait()
            self.pulse()
            self.wait()
            self.flicker()
            self.wait()
            self.reset()


tree = Tree()
tree.go()
