import pathway as pw

# 1. Ingestion: Connect to the "Sensor" data
# This watches the CSV file for new lines in real-time
input_table = pw.io.csv.read(
    "water_data.csv", 
    mode="streaming", 
    schema=pw.schema_from_csv("water_data.csv")
)

# 2. Transformation (The Logic)
# We filter for any water level above 45cm
alert_table = input_table.filter(pw.this.water_level > 45)

# 3. Output
# When an alert is found, write it to a new file called "alerts.csv"
pw.io.csv.write(alert_table, "alerts.csv")

# Run the pipeline
print("Pathway Engine is running... Monitoring for floods.")
pw.run()