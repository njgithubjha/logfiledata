import re
from datetime import datetime
import matplotlib.pyplot as plt

# Define the regular expression to match log entries
log_entry_regex = r'^(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"$'

# Define lists to store data
timestamps = []
ip_addresses = []

# Open the log file and process each line
with open("formate.log", "r") as f:
    for line in f:
        # Use regex to extract data from the log entry
        match = re.match(log_entry_regex, line.strip())
        if match is not None:
            ip_address = match.group(1)
            timestamp = datetime.strptime(match.group(2), '%d/%b/%Y:%H:%M:%S %z')
            
            # Add data to the lists
            ip_addresses.append(ip_address)
            timestamps.append(timestamp)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Plot the data as a scatter plot
ax.scatter(timestamps, ip_addresses)

# Set the x-axis label and rotate the tick labels for better readability
ax.set_xlabel('Time')
plt.xticks(rotation=45)

# Set the y-axis label
ax.set_ylabel('IP Address')

# Set the title of the plot
ax.set_title('IP Addresses by Time')

# Show the plot
plt.show()
