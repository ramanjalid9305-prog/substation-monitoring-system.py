import random
import time
from datetime import datetime

# -----------------------------
# SUBSTATION LIMITS
# -----------------------------
VOLTAGE_MIN = 210
VOLTAGE_MAX = 250

CURRENT_MAX = 100

FREQUENCY_MIN = 49
FREQUENCY_MAX = 51

TRANSFORMER_TEMP_MAX = 85

LOAD_MAX = 90


# -----------------------------
# SENSOR SIMULATION
# -----------------------------
def read_sensors():
    """Generate simulated substation sensor readings."""

    voltage = random.uniform(200, 260)
    current = random.uniform(20, 120)
    frequency = random.uniform(48, 52)
    temperature = random.uniform(50, 100)
    load = random.uniform(40, 100)

    return {
        "voltage": voltage,
        "current": current,
        "frequency": frequency,
        "temperature": temperature,
        "load": load
    }


# -----------------------------
# MONITORING FUNCTION
# -----------------------------
def monitor_substation(data):

    alarms = []

    if data["voltage"] < VOLTAGE_MIN:
        alarms.append("LOW VOLTAGE")

    elif data["voltage"] > VOLTAGE_MAX:
        alarms.append("HIGH VOLTAGE")

    if data["current"] > CURRENT_MAX:
        alarms.append("OVER CURRENT")

    if data["frequency"] < FREQUENCY_MIN:
        alarms.append("LOW FREQUENCY")

    elif data["frequency"] > FREQUENCY_MAX:
        alarms.append("HIGH FREQUENCY")

    if data["temperature"] > TRANSFORMER_TEMP_MAX:
        alarms.append("HIGH TRANSFORMER TEMPERATURE")

    if data["load"] > LOAD_MAX:
        alarms.append("OVERLOAD")

    return alarms


# -----------------------------
# LOGGING FUNCTION
# -----------------------------
def log_event(data, alarms):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("substation_log.txt", "a") as file:

        file.write(
            f"{current_time} | "
            f"Voltage={data['voltage']:.2f} V | "
            f"Current={data['current']:.2f} A | "
            f"Frequency={data['frequency']:.2f} Hz | "
            f"Temperature={data['temperature']:.2f} °C | "
            f"Load={data['load']:.2f} % | "
            f"Alarms={', '.join(alarms) if alarms else 'NONE'}\n"
        )


# -----------------------------
# DISPLAY FUNCTION
# -----------------------------
def display_status(data, alarms):

    print("\n" + "=" * 60)
    print("             SUBSTATION MONITORING SYSTEM")
    print("=" * 60)

    print(f"Voltage              : {data['voltage']:.2f} V")
    print(f"Current              : {data['current']:.2f} A")
    print(f"Frequency            : {data['frequency']:.2f} Hz")
    print(f"Transformer Temp.    : {data['temperature']:.2f} °C")
    print(f"Load                 : {data['load']:.2f} %")

    print("-" * 60)

    if alarms:
        print("STATUS: ⚠️ ALARM")
        print("ALARMS:")

        for alarm in alarms:
            print(f"  🔴 {alarm}")

    else:
        print("STATUS: 🟢 NORMAL")
        print("No alarms detected.")

    print("=" * 60)


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():

    print("Starting Substation Monitoring System...")

    try:

        while True:

            sensor_data = read_sensors()

            alarms = monitor_substation(sensor_data)

            display_status(sensor_data, alarms)

            log_event(sensor_data, alarms)

            print("\nNext reading in 3 seconds...")
            time.sleep(3)

    except KeyboardInterrupt:

        print("\nMonitoring system stopped by user.")


# -----------------------------
# PROGRAM ENTRY
# -----------------------------
if __name__ == "__main__":
    main()
