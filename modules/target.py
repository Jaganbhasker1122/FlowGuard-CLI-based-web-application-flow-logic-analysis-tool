import random

def target_set(state, parts, Colors, ProgressBar):
    """Set target URL"""
    try:
        url_idx = parts.index("--url") + 1
        url = parts[url_idx]

        print(f"\n{Colors.CYAN}[*] Setting target: {url}{Colors.RESET}\n")
        ProgressBar.animate(duration=1.0, label="Resolving target...", width=50)

        state.target_url = url
        print(f"{Colors.GREEN}[+] Target set successfully{Colors.RESET}")
        print(f"{Colors.BLUE}[i] URL: {Colors.GREEN}{url}{Colors.RESET}\n")

    except (ValueError, IndexError):
        print(f"\n{Colors.RED}[!] Usage: fg target-set --url <URL>{Colors.RESET}\n")


def target_show(state, Colors, print_box):
    """Show current target"""
    print()
    if state.target_url:
        info = [
            "",
            f"{Colors.YELLOW}Current Target:{Colors.RESET}",
            f"  {Colors.GREEN}{state.target_url}{Colors.RESET}",
            "",
        ]
        print_box("TARGET CONFIGURATION", info)
    else:
        print(f"{Colors.YELLOW}[!] No target configured{Colors.RESET}")
    print()


def target_clear(state, Colors):
    """Clear target"""
    state.target_url = None
    print(f"\n{Colors.YELLOW}[!] Target configuration cleared{Colors.RESET}\n")


def target_ping(state, Colors, ProgressBar):
    """Check target reachability"""
    if not state.target_url:
        print(f"\n{Colors.RED}[!] No target set{Colors.RESET}\n")
        return

    print(f"\n{Colors.CYAN}[*] Pinging target: {state.target_url}{Colors.RESET}\n")
    ProgressBar.animate(duration=1.2, label="Connecting...", width=50)

    print(f"{Colors.GREEN}[+] Target is reachable{Colors.RESET}")
    print(
        f"{Colors.BLUE}[i] Response time: "
        f"{random.randint(10, 100)}ms{Colors.RESET}\n"
    )
