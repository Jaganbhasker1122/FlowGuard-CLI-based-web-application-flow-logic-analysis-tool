# modules/proxy.py

def proxy_start(state, Colors, ProgressBar):
    """Start proxy (mocked)"""
    print(f"\n{Colors.CYAN}[*] Starting proxy engine...{Colors.RESET}\n")
    ProgressBar.animate(duration=1.5, label="Binding to port 8080...", width=50)

    state.proxy_running = True
    print(f"{Colors.GREEN}[+] Proxy started successfully{Colors.RESET}")
    print(f"{Colors.BLUE}[i] Address: 127.0.0.1:8080{Colors.RESET}\n")


def proxy_stop(state, Colors, ProgressBar):
    """Stop proxy (mocked)"""
    if not state.proxy_running:
        print(f"\n{Colors.YELLOW}[!] Proxy is not running{Colors.RESET}\n")
        return

    print(f"\n{Colors.CYAN}[*] Stopping proxy...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.8, label="Shutting down...", width=50)

    state.proxy_running = False
    print(f"{Colors.YELLOW}[!] Proxy stopped{Colors.RESET}\n")


def proxy_status(state, Colors, print_box):
    """Show proxy status"""
    status = "Running" if state.proxy_running else "Stopped"
    color = Colors.GREEN if state.proxy_running else Colors.RED

    info = [
        "",
        f"{Colors.YELLOW}Proxy Status:{Colors.RESET} {color}{status}{Colors.RESET}",
    ]

    if state.proxy_running:
        info.append(
            f"{Colors.YELLOW}Address:{Colors.RESET} "
            f"{Colors.BLUE}127.0.0.1:8080{Colors.RESET}"
        )
        info.append(
            f"{Colors.YELLOW}Intercepting:{Colors.RESET} "
            f"{Colors.GREEN}Enabled{Colors.RESET}"
        )

    info.append("")

    print()
    print_box("PROXY STATUS", info)


def proxy_config(Colors, print_box):
    """Show proxy configuration"""
    info = [
        "",
        f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
        f"{Colors.YELLOW}Host:{Colors.RESET}                    {Colors.GREEN}127.0.0.1{Colors.RESET}",
        f"{Colors.YELLOW}Port:{Colors.RESET}                    {Colors.GREEN}8080{Colors.RESET}",
        f"{Colors.YELLOW}SSL Pass-through:{Colors.RESET}         {Colors.GREEN}Enabled{Colors.RESET}",
        f"{Colors.YELLOW}Request Interception:{Colors.RESET}     {Colors.GREEN}Enabled{Colors.RESET}",
        f"{Colors.YELLOW}Response Modification:{Colors.RESET}    {Colors.GREEN}Enabled{Colors.RESET}",
        f"{Colors.YELLOW}Connection Timeout:{Colors.RESET}      {Colors.GREEN}30 seconds{Colors.RESET}",
        f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
        "",
    ]

    print()
    print_box("PROXY CONFIGURATION", info)
