import sys
import os
from pathlib import Path

package_dir = Path(__file__).parent.absolute()
if str(package_dir) not in sys.path:
    sys.path.append(str(package_dir)) 
try:
    from . import run
except ImportError:
    import run
def start():
    run.execute()
if __name__ == "__main__":
    start()
