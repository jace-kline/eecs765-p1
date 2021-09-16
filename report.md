# EECS 765 Project 1

## Introduction

The purpose of this programming assignment is to practice the development and execution of a remote buffer overflow attack on a vulnerable webserver deployed on RedHat 8 Linux. We also explore an additional attack on RedHat 9 that emplmitigation technique called stack address randomization.

## Environment Setup

The first step in developing an exploit is properly configuring an environment that accurately portrays the environment used in a live attack scenario. We first set up an environment following the constraints given in the programming assignment description. We create a NAT subnet 192.168.180.0 in VMWare and assign the static IP addresses of 192.168.180.10, 192.168.180.40, and 192.168.180.50 to the Kali, RedHat 8, and RedHat 9 VMs, respectively. Next, we ensure that each machine can reach all the others via netcat. We also start the nweb servers on the RedHat 8 and RedHat 9 machines by navigating to the /root directory and running `./nweb 8888 .`, and then we ensure that the webservers are accessible from the Kali VM. For efficiency of attack development, we also set up SSH for each of these machines.

## Running the Exploit

The exploits work in both the RedHat 8 and RedHat 9 attack scenarios. The IP addresses used in the exploits were identical to those specified in the PA1 description (shown in the environment setup above). We use port 8228 on the Kali VM to listen for the reverse shell connection. The steps for running each of the exploits are below. We assume that for each attack, the environment is properly configured and the victim VM is running the nweb webserver on port 8888. We assume that the working directory on the Kali VM is at the root of the project code.

First, navigate to the target exploit folder in the current shell. For the RedHat 8 exploit, run `cd redhat8`. For the RedHat 9 exploit, run `cd redhat9`. Each of these directories has the same structure and includes `exploit.sh` and `generate_shellcode.py` files specific to each of these attacks.

Next, open another shell on the Kali machine. In this shell, we want to set up a listener to receive the callback TCP connection from the reverse shell that will be spawned on the victim during the attack. We use netcat to achieve this, and we specify port 8228 to listen on.

```nc -nlvp 8228```

Next, we return back to the other shell to run the exploit. Run the `exploit.sh` shell script to generate and send the malicious input to the webserver on the victim machine. The contents of `exploit.sh` are shown in the 'Developing the Exploit' section below. Specifically, we run the following command:

```./exploit.sh```

After sending the malicious input above, return attention to the listener shell. After a slight delay, there should be a message that indicates a connection initiated from the victim machine. The RedHat 8 exploit should result in a TCP connection from IP address 192.168.180.40. The RedHat 9 exploit should result in a TCP connection from IP address 192.168.180.50. In this listener shell, run some test commands such as `whoami` and `ls` to verify that the reverse shell (as root user) has been established successfully.  Below, we show that the results from successful exploits targeted at both the RedHat 8 and RedHat 9 victim machines.

![RedHat 8 Exploit](./screenshots/redhat8-exploit.png?raw=true)
![RedHat 9 Exploit](./screenshots/redhat9-exploit.png?raw=true)

## Developing the Exploit

### Malicious Input Structure

Describe the structure of the input, explain why you chose this structure and what you are hoping to achieve.

### Malicious Input Parameters

What are the paramaters you need to determine and why? e.g., little or big endian architecture, buffer length, distance to saved_EIP, value stored in saved_EIP, etc.
How did you determine the values for the above-mentioned paramaters?

### Generating the Malicious Input

What programming language did you use?
How did you construct the malicious input? (brief description)

## References and Collaborations

Specify your online or hardcopy sources of information (especially if your exploit is based on someone else's source code - should NOT be a classmate)
List the people that you discussed the programming assignment with. Also, add a very brief description of what you discussed with each individual. Don't forget that programming assignments are individual assignments
