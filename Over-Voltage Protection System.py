# Over-Voltage-Protection-System
import time

# Over-voltage protection settings
SAFE_VOLTAGE = 240.0       # Maximum safe voltage
RESET_VOLTAGE = 230.0      # Voltage required to reconnect
CHECK_INTERVAL = 1          # Seconds

load_connected = True

print("======================================")
print("     OVER-VOLTAGE PROTECTION SYSTEM")
print("======================================")
print(f"Maximum Safe Voltage : {SAFE_VOLTAGE} V")
print("--------------------------------------")

while True:
    try:
        voltage = float(input("Enter measured voltage (V): "))

        print(f"Measured Voltage: {voltage:.2f} V")

        # Over-voltage condition
        if voltage > SAFE_VOLTAGE:
            if load_connected:
                load_connected = False
                print("⚠️ OVER-VOLTAGE DETECTED!")
                print("🔴 Load disconnected for protection.")
            else:
                print("🔴 Load remains disconnected.")

        # Safe voltage condition
        elif voltage <= RESET_VOLTAGE:
            if not load_connected:
                load_connected = True
                print("🟢 Voltage is normal.")
                print("🟢 Load connected.")
            else:
                print("🟢 Voltage is normal.")
                print("🟢 Load is connected.")

        # Voltage between reset and trip levels
        else:
            if load_connected:
                print("🟡 Voltage is within operating range.")
                print("🟢 Load is connected.")
            else:
                print("🟡 Voltage is below trip level but waiting for safe reset voltage.")
                print("🔴 Load remains disconnected.")

        print("--------------------------------------")
        time.sleep(CHECK_INTERVAL)

    except ValueError:
        print("❌ Please enter a valid voltage value.")

    except KeyboardInterrupt:
        print("\nSystem stopped.")
        break
