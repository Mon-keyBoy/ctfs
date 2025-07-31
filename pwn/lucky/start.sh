#!/bin/bash
socat -T 300 TCP-LISTEN:15252,reuseaddr,fork EXEC:/home/prob/prob,su=prob,stderr
