# modules/flow.py

def flow_analyze(state, Colors, ProgressBar):
    """Analyze HTTP request flows (mocked)"""
    print(f"\n{Colors.CYAN}[*] Analyzing request flows...{Colors.RESET}\n")
    ProgressBar.animate(duration=1.5, label="Analyzing HTTP sequences...", width=50)

    # Mock detected flows
    state.flows = [
        {"name": "Authentication Flow", "steps": 3, "status": "Complete"},
        {"name": "User Session Flow", "steps": 5, "status": "Complete"},
        {"name": "API Call Sequence", "steps": 7, "status": "Complete"},
        {"name": "Logout Flow", "steps": 2, "status": "Complete"},
    ]

    print(f"{Colors.GREEN}[+] Flow analysis complete{Colors.RESET}")
    print(f"{Colors.BLUE}[i] Detected {len(state.flows)} unique flows{Colors.RESET}\n")


def flow_show(state, Colors, ProgressBar, print_box):
    """Display detected flows"""
    print(f"\n{Colors.CYAN}[*] Retrieving flow data...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.8, label="Loading...", width=50)

    if not state.flows:
        print(f"{Colors.YELLOW}[!] No flows available. Run flow-analyze first.{Colors.RESET}\n")
        return

    info = [
        "",
        f"{Colors.B_MAGENTA}Detected Application Flows{Colors.RESET}",
        "",
    ]

    for flow in state.flows:
        info.append(f"{Colors.MAGENTA}●{Colors.RESET} {Colors.BOLD}{flow['name']}{Colors.RESET}")
        info.append(
            f"  {Colors.YELLOW}Steps:{Colors.RESET} "
            f"{Colors.B_CYAN}{flow['steps']}{Colors.RESET} | "
            f"{Colors.YELLOW}Status:{Colors.RESET} "
            f"{Colors.GREEN}{flow['status']}{Colors.RESET}"
        )
        info.append("")

    print()
    print_box("FLOW ANALYSIS", info)


def flow_export(state, parts, Colors, ProgressBar):
    """Export flows (mocked)"""
    try:
        format_idx = parts.index("--format") + 1
        format_type = parts[format_idx]

        print(f"\n{Colors.CYAN}[*] Exporting flows as {format_type}...{Colors.RESET}\n")
        ProgressBar.animate(duration=1.0, label="Exporting...", width=50)

        print(f"{Colors.GREEN}[+] Flows exported successfully{Colors.RESET}")
        print(f"{Colors.BLUE}[i] Format: {format_type}{Colors.RESET}\n")

    except (ValueError, IndexError):
        print(f"\n{Colors.RED}[!] Usage: fg flow-export --format <format>{Colors.RESET}\n")


def flow_reset(state, Colors, ProgressBar):
    """Reset flow analysis state"""
    print(f"\n{Colors.CYAN}[*] Resetting flow state...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.6, label="Clearing...", width=50)

    state.flows = []
    print(f"{Colors.YELLOW}[!] Flow state reset{Colors.RESET}\n")
