# modules/report.py

from datetime import datetime

def report_generate(state, Colors, ProgressBar):
    """Generate security report (mocked)"""
    print(f"\n{Colors.CYAN}[*] Generating security report...{Colors.RESET}\n")
    ProgressBar.animate(duration=2.0, label="Compiling findings...", width=50)

    state.current_report = {
        "date": datetime.now().isoformat(),
        "vulnerabilities": 8,
        "high_severity": 3,
        "medium_severity": 5,
    }

    print(f"{Colors.GREEN}[+] Report generated successfully{Colors.RESET}\n")


def report_show(state, Colors, print_box):
    """Display current report"""
    if not state.current_report:
        print(f"\n{Colors.YELLOW}[!] No report generated{Colors.RESET}\n")
        return

    report = state.current_report

    info = [
        "",
        f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
        f"{Colors.YELLOW}Generated:{Colors.RESET}       "
        f"{Colors.GREEN}{report['date']}{Colors.RESET}",
        f"{Colors.YELLOW}Vulnerabilities:{Colors.RESET}  "
        f"{Colors.RED}{report['vulnerabilities']}{Colors.RESET}",
        f"{Colors.YELLOW}High Severity:{Colors.RESET}    "
        f"{Colors.B_RED}{report['high_severity']}{Colors.RESET}",
        f"{Colors.YELLOW}Medium Severity:{Colors.RESET}  "
        f"{Colors.B_YELLOW}{report['medium_severity']}{Colors.RESET}",
        f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
        "",
    ]

    print()
    print_box("SECURITY REPORT", info)


def report_export(state, parts, Colors, ProgressBar):
    """Export report (mocked)"""
    try:
        format_idx = parts.index("--format") + 1
        format_type = parts[format_idx]

        out_idx = parts.index("--out") + 1
        output_dir = parts[out_idx]

        print(f"\n{Colors.CYAN}[*] Exporting report as {format_type}...{Colors.RESET}\n")
        ProgressBar.animate(duration=1.2, label="Exporting...", width=50)

        print(f"{Colors.GREEN}[+] Report exported successfully{Colors.RESET}")
        print(
            f"{Colors.BLUE}[i] File: "
            f"{output_dir}report_{datetime.now().strftime('%Y_%m_%d')}.{format_type}"
            f"{Colors.RESET}\n"
        )

    except (ValueError, IndexError):
        print(
            f"\n{Colors.RED}[!] Usage: "
            f"fg report-export --format <format> --out <dir>{Colors.RESET}\n"
        )
