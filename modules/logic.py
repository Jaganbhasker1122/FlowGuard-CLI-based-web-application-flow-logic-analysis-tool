# modules/logic.py

import time

def logic_test(state, Colors):
    """Run business logic vulnerability tests (mocked)"""
    print(f"\n{Colors.CYAN}[*] Running business logic tests...{Colors.RESET}\n")

    tests = [
        ("Admin Bypass Detection", "PASS"),
        ("Privilege Escalation Check", "PASS"),
        ("Parameter Tampering Test", "FAIL"),
        ("Session Fixation Test", "PASS"),
        ("Insecure Direct References", "FAIL"),
    ]

    passed = failed = 0

    for test, result in tests:
        result_color = Colors.GREEN if result == "PASS" else Colors.RED
        result_icon = "✓" if result == "PASS" else "✗"

        print(
            f"  {result_color}{result_icon}{Colors.RESET} "
            f"{test:<35} {result_color}[{result}]{Colors.RESET}"
        )
        time.sleep(0.2)

        if result == "PASS":
            passed += 1
        else:
            failed += 1

    print()
    print(
        f"{Colors.BLUE}[i] Results: "
        f"{Colors.GREEN}{passed} passed{Colors.RESET}, "
        f"{Colors.RED}{failed} failed{Colors.RESET}\n"
    )


def logic_rules(state, Colors, print_box):
    """Display available logic rules"""
    info = [
        "",
        f"{Colors.B_MAGENTA}Available Security Rules{Colors.RESET}",
        "",
    ]

    for rule, enabled in state.logic_rules.items():
        status = (
            f"{Colors.GREEN}[ENABLED]{Colors.RESET}"
            if enabled
            else f"{Colors.RED}[DISABLED]{Colors.RESET}"
        )
        rule_name = rule.replace("_", " ").title()
        info.append(
            f"{Colors.YELLOW}●{Colors.RESET} "
            f"{Colors.CYAN}{rule_name:<30}{Colors.RESET} {status}"
        )

    info.append("")

    print()
    print_box("LOGIC RULES", info)


def logic_enable(state, parts, Colors):
    """Enable a logic rule"""
    try:
        rule_idx = parts.index("--rule") + 1
        rule_name = parts[rule_idx]

        if rule_name in state.logic_rules:
            state.logic_rules[rule_name] = True
            print(f"\n{Colors.GREEN}[+] Rule enabled: {rule_name}{Colors.RESET}\n")
        else:
            print(f"\n{Colors.RED}[!] Rule not found: {rule_name}{Colors.RESET}\n")

    except (ValueError, IndexError):
        print(f"\n{Colors.RED}[!] Usage: fg logic-enable --rule <RULE_NAME>{Colors.RESET}\n")


def logic_disable(state, parts, Colors):
    """Disable a logic rule"""
    try:
        rule_idx = parts.index("--rule") + 1
        rule_name = parts[rule_idx]

        if rule_name in state.logic_rules:
            state.logic_rules[rule_name] = False
            print(f"\n{Colors.YELLOW}[!] Rule disabled: {rule_name}{Colors.RESET}\n")
        else:
            print(f"\n{Colors.RED}[!] Rule not found: {rule_name}{Colors.RESET}\n")

    except (ValueError, IndexError):
        print(f"\n{Colors.RED}[!] Usage: fg logic-disable --rule <RULE_NAME>{Colors.RESET}\n")
