# modules/capture.py

def capture_start(state, Colors, ProgressBar):
    """Start traffic capture (mocked)"""
    print(f"\n{Colors.CYAN}[*] Starting traffic capture...{Colors.RESET}\n")
    ProgressBar.animate(duration=1.0, label="Initializing sniffer...", width=50)

    state.capture_running = True
    print(f"{Colors.GREEN}[+] Traffic capture started{Colors.RESET}\n")


def capture_stop(state, Colors, ProgressBar):
    """Stop traffic capture (mocked)"""
    if not state.capture_running:
        print(f"\n{Colors.YELLOW}[!] Capture not running{Colors.RESET}\n")
        return

    print(f"\n{Colors.CYAN}[*] Stopping capture...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.8, label="Finalizing...", width=50)

    state.capture_running = False
    print(f"{Colors.YELLOW}[!] Capture stopped{Colors.RESET}\n")


def capture_list(state, Colors, ProgressBar, print_box):
    """List captured requests (mocked)"""
    print(f"\n{Colors.CYAN}[*] Generating capture list...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.8, label="Processing...", width=50)

    # Mock sample data
    sample_requests = [
        ("GET", "/api/users", "200", "1.2s"),
        ("POST", "/api/login", "200", "0.8s"),
        ("GET", "/dashboard", "200", "2.1s"),
        ("PUT", "/api/profile", "400", "0.5s"),
        ("DELETE", "/api/session", "204", "0.3s"),
    ]

    info = [
        "",
        f"{Colors.B_MAGENTA}Captured Requests ({len(sample_requests)}){Colors.RESET}",
        "",
        f"{Colors.B_CYAN}ID   Method   Path                   Status   Time{Colors.RESET}",
        f"{Colors.B_CYAN}─────────────────────────────────────────────────────{Colors.RESET}",
    ]

    for idx, (method, path, status, time_taken) in enumerate(sample_requests, 1):
        status_color = Colors.GREEN if status.startswith("2") else Colors.RED
        info.append(
            f"  {idx}  {Colors.B_CYAN}{method}{Colors.RESET:<6} "
            f"{Colors.MAGENTA}{path}{Colors.RESET:<22} "
            f"{status_color}{status:<6}{Colors.RESET} "
            f"{Colors.YELLOW}{time_taken}{Colors.RESET}"
        )

    info.append("")

    print()
    print_box("TRAFFIC CAPTURE", info)


def capture_clear(state, Colors, ProgressBar):
    """Clear captured traffic (mocked)"""
    print(f"\n{Colors.CYAN}[*] Clearing captured data...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.6, label="Erasing...", width=50)

    state.captured_requests = []
    print(f"{Colors.YELLOW}[!] Capture data cleared{Colors.RESET}\n")
