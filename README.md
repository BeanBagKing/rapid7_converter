# rapid7_converter
Rapid7's Nexpose and InsightVM converts IP ranges (CIDR blocks) into their own range format for sites. This converts them back.

# What does Nexpose/InsightVM do?
When adding a range to one of these tools, they will incriment the lowest IP by one, decrement the highest by one, and insert their own formatting as comma (with space) delimited and space-dash-space for ranges, like so...
```
192.168.4.0/24 192.168.8.0/24
```
becomes...
```
192.168.4.1 - 192.168.4.254, 192.168.8.1 - 192.168.8.254
```
This is a bit annoying to me, so I created a short script to convert these back if I need to use or reference the ranges elsewhere.

# How?
I start by standardizing the format a bit, placing each range on it's own line, removing spaces, and removing any blank lines

Then, via copy/paste code (I know, it's terrible, this is quick and dirty) I...
1. Split the range using the -
2. Decrement the lowest IP and incriement the highest to get us back to the original CIDR range
3. Use the ipaddress library in python3 to convert this to a range (or ranges)
4. Print these ranges as space delimited (nmap/masscan), comma delimited, and newline delimited.
5. I also used the library to total the number of addresses in all of the ranges.
