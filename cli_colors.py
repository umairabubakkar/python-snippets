class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def success(msg): print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")
def error(msg): print(f"{Colors.RED}✗ {msg}{Colors.RESET}")
def warning(msg): print(f"{Colors.YELLOW}⚠ {msg}{Colors.RESET}")
def info(msg): print(f"{Colors.BLUE}ℹ {msg}{Colors.RESET}")
def bold(msg): print(f"{Colors.BOLD}{msg}{Colors.RESET}")
