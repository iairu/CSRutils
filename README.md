# CSR (SIP) Utilities for OpenCore configuration

This is a set of utilities, so you don't have to leave your system exposed and misbehaving: Set the correct SIP for your use-case instead of completely disabling it.

> Ever wondered how to turn something like 
>
> `csrutil enable --without debug --without fs` (example from unaffiliated MacForge software)
>
> to `CSR_ALLOW_TASK_FOR_PID & CSR_ALLOW_UNRESTRICTED_FS` 
>
> to `0x6` 
>
> to `csr-active-config: 06000000`? 
>
> Look no further, this repository has the answer!

## Guide

1. Use `csrstat` (compile using `clang csrstat.c` or `gcc csrstat.c`) to remap `csrutil` arguments to `CSR_ALLOW` constants
2. Use `python3 BitmaskDecode.py` to get the `0xXXX` hex value for your combination of chosen constants
3. Use `python3 sip-convert.py 0xXXX` which uses code taken from OCLP to convert hex to `csr-active-config`; replace `0xXXX` with your hex value
4. Use Xplist, ProperTree or similar software to edit your OpenCore `config.plist` configuration with your newly obtained value for `csr-active-config` in `NVRAM > Add > 7C436110-AB2A-4BBB-A880-FE41995C9F82`. Don't use Notepad/TextEdit/vi/nano/... because editing the file raw exposes the `csr-active-config` value in a different (unsupported) format.
5. Enjoy!

## Sources

This repository is a partial compilation from following unaffiliated repositories:

- https://github.com/JayBrown/csrstat-NG under MIT License: Update of Pike R. Alpha's original csrstat CLI by Joss Brown
- https://github.com/corpnewt/BitmaskDecode under MIT License by CorpNewt
- https://github.com/dortania/OpenCore-Legacy-Patcher by Dhinak G, Mykola Grymalyuk, and individual contributors.

See LICENSE for a list of all licenses. This product includes software developed by Dortania and OpenCore Legacy Patcher contributors.