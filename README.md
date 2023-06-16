# Paragen
Common Vulnerability Report mail generator for VM Tools
Suppose you have few vulnerabilities that keep on repeating then just store them here, instead of retyping / copying them into your report everytime

Usage:
add a list of commonly occuring vulnerabilities, keep them between @
To generate run the file, type the last two octets of IP,
type comma sepearted unique word in sentence 
 
example:
• SSL Medium Strength Cipher Suites Supported (SWEET32). Reconfigure to avoid use of DES/3DES ciphers.
• Disable TLS 1.0
• Disable TLS 1.1

Above are list of vulnerabilities,
i wanna add all tls and ssl vuln in my report

so i'll be like:

PS D:\scripts\Paragen> python.exe .\paragen.py
Enter IP: 0.1
Enter comma-separated words: ssl,tls
Please find the vulnerability scan results for 192.168.0.1 below:

• SSL Medium Strength Cipher Suites Supported (SWEET32). Reconfigure to avoid use of DES/3DES ciphers.

• Disable TLS 1.0

• Disable TLS 1.1


If you understand, you understand, i can't explain it any more simply.