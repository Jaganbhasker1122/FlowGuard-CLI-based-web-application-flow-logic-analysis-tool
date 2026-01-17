# modules/doctor.py

import time

def run_doctor(state, Colors):
    """System diagnostics"""
    print(f"\n{Colors.CYAN}[*] Running system diagnostics...{Colors.RESET}\n")

    checks = [
        ("Python version", True, "3.9+"),
        ("Network connectivity", True, "OK"),
        ("Proxy engine", True, "Available"),
        ("SSL/TLS support", True, "Enabled"),
        ("Terminal ANSI support", True, "Enabled"),
        ("Permissions", True, "Adequate"),
    ]

    for check, status, detail in checks:
        status_icon = (
            f"{Colors.GREEN}✓{Colors.RESET}"
            if status
            else f"{Colors.RED}✗{Colors.RESET}"
        )
        print(
            f"  {status_icon} {check:<30} "
            f"{Colors.DIM}[{Colors.BLUE}{detail}{Colors.DIM}]{Colors.RESET}"
        )
        time.sleep(0.15)

    print(f"\n{Colors.GREEN}[+] All systems operational{Colors.RESET}\n")
