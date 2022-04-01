from machine import ADC
import time
adc = ADC (27)

v1=0
t1=0
while True:
    cacapedopis = adc.read_u16()
    v1 = cacapedopis * 3.3
    v1 = v1/65535
    t1 = v1/0.01
    time.sleep(1)
    
    print ("Temperatura: {:.2f}".format(t1))
    