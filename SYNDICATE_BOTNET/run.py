import asyncio
import sys
import os
try:
    import bux 
except ImportError as e:
    print(f"\033[1;31m[!] Critical Error: Failed to import binary core 'bux'.")
    print(f"\033[1;33m[*] Details: {e}")
    print("\033[1;37m[*] Make sure you are using Python 3.12 and the .so file is in the current directory.")
    sys.exit(1)
def execute():
    try:
        if sys.version_info[:2] != (3, 12):
            print(f"\033[1;31m[!] Version Mismatch: This binary requires Python 3.12.")
            print(f"\033[1;33m[*] Your version: {sys.version_info[0]}.{sys.version_info[1]}")
            sys.exit(1)
        asyncio.run(bux.validate_license())

    except AttributeError:
        print("\033[1;31m[!] Execution Error: Function 'main' not found in the binary module.")
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Aborted by user. Exiting safely...")
        sys.exit(0)
    except Exception as e:
        print(f"\033[1;31m[!] Unexpected Runtime Error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    execute()
