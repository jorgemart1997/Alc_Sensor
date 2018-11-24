import sys, time
import math
from MCP3008 import MCP3008

try:
    print("Press CTRL+C to abort.")

    while True:
        MQ_PIN = 0
        self.MQ_PIN = analogPin // equivalent to sensorValue
        sensor_volt = self.MQ_PIN/(1024*5.0);
        RS_gas = (5.0 - sensor_volt)/sensor_volt;       //omit * RL

        ratio = RS_gas/1.5;     //ratio = RS/RO

        sys.stdout.write("Sensor Voltage: ");
        sys.stdout.write(sensor_volt);
        sys.stdout.write("\n")

        sys.stdout.write("RS_ratio = ")
        sys.stdout.write(RS_gas)
        sys.stdout.write("\n")

        sys.stdout.write("Rs/R0 = ")
        sys.stdout.write(ratio);
        sys.stdout.write("\n")

        BAC = (ratio - 1.34)/(-0.37);
        sys.stdout.write("Alcohol Level = ");
        sys.stdout.write(BAC/10);
        sys.stdout.write(" BAC");
        sys.stdout.write("\n")

        sys.stdout.flush()

        if (BAC > 0.08){
            Serial.println("Alcohol breath detected to be above 0.08.\nPerson is intoxicated.");
        }
        else:
            return 0

        time.sleep(0.15)

except:
    print("\nAbort by user")
