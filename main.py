import subprocess

def scan_wifi():
    # Use the subprocess module to run the "arp -a" command
    result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE)

    # Split the output into a list of lines
    lines = result.stdout.decode().split("\n")

    # Iterate through the lines and extract the IP addresses
    for line in lines:
        words = line.split()
        if len(words) == 3:
            print(words[0])

# Call the scan_wifi function
scan_wifi()

