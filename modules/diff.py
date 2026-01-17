# modules/diff.py

def diff_run(state, parts, Colors, ProgressBar, print_box):
    """Compare two responses (mocked)"""
    try:
        req_a_idx = parts.index("--req-a") + 1
        req_b_idx = parts.index("--req-b") + 1
        req_a = parts[req_a_idx]
        req_b = parts[req_b_idx]

        print(
            f"\n{Colors.CYAN}[*] Comparing requests "
            f"#{req_a} and #{req_b}...{Colors.RESET}\n"
        )
        ProgressBar.animate(duration=1.0, label="Analyzing...", width=50)

        info = [
            "",
            f"{Colors.B_MAGENTA}Response Differences{Colors.RESET}",
            "",
            f"{Colors.YELLOW}+{Colors.RESET} "
            f"{Colors.GREEN}Line 45: New user ID in response{Colors.RESET}",
            f"{Colors.RED}-{Colors.RESET} "
            f"{Colors.YELLOW}Line 63: Missing authorization header{Colors.RESET}",
            f"{Colors.MAGENTA}~{Colors.RESET} "
            f"{Colors.BLUE}Line 78: Response time variation: 120ms{Colors.RESET}",
            "",
        ]

        print()
        print_box("RESPONSE COMPARISON", info)

    except (ValueError, IndexError):
        print(
            f"\n{Colors.RED}[!] Usage: "
            f"fg diff-run --req-a <ID> --req-b <ID>{Colors.RESET}\n"
        )


def diff_summary(state, Colors, ProgressBar, print_box):
    """Summarize response differences (mocked)"""
    print(f"\n{Colors.CYAN}[*] Generating diff summary...{Colors.RESET}\n")
    ProgressBar.animate(duration=0.8, label="Summarizing...", width=50)

    info = [
        "",
        f"{Colors.YELLOW}Similarities:{Colors.RESET}      "
        f"{Colors.GREEN}87%{Colors.RESET}",
        f"{Colors.YELLOW}Differences:{Colors.RESET}       "
        f"{Colors.RED}13%{Colors.RESET}",
        f"{Colors.YELLOW}Notable Changes:{Colors.RESET}   "
        f"{Colors.YELLOW}5 detected{Colors.RESET}",
        "",
    ]

    print()
    print_box("COMPARISON SUMMARY", info)
