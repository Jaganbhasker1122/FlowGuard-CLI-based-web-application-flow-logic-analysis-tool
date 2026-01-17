#!/usr/bin/env python3
"""
FlowGuard v1.0 SUPREME - Advanced Web Application Security Testing Framework

"""

import os
import sys
import time
import random
import difflib
from datetime import datetime
from core.context import AppState
from modules.target import (
    target_set,
    target_show,
    target_clear,
    target_ping
)
from modules.doctor import run_doctor
from modules.proxy import (
    proxy_start,
    proxy_stop,
    proxy_status,
    proxy_config
)
from modules.capture import (
    capture_start,
    capture_stop,
    capture_list,
    capture_clear
)
from modules.flow import (
    flow_analyze,
    flow_show,
    flow_export,
    flow_reset
)
from modules.logic import (
    logic_test,
    logic_rules,
    logic_enable,
    logic_disable
)
from modules.session import (
    session_analyze,
    session_reuse_test,
    session_invalidate_test
)
from modules.diff import (
    diff_run,
    diff_summary
)
from modules.report import (
    report_generate,
    report_show,
    report_export
)





# ============================================================================
# ANSI COLOR CODES & STYLES
# ============================================================================

class Colors:
    # Primary Colors
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    BLACK = '\033[30m'
    
    # Bright Colors
    B_CYAN = '\033[1;96m'
    B_GREEN = '\033[1;92m'
    B_RED = '\033[1;91m'
    B_YELLOW = '\033[1;93m'
    B_MAGENTA = '\033[1;95m'
    B_BLUE = '\033[1;94m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Reset
    RESET = '\033[0m'

class ColorfulProgressBar:
    """Advanced colorful progress bar"""
    
    @staticmethod
    def animate(duration=2.0, label="INITIALIZING", width=60):
        """Display animated colorful progress bar"""
        start = time.time()
        steps = int(duration * 20)
        colors = [Colors.CYAN, Colors.B_CYAN, Colors.GREEN, Colors.B_GREEN]
        
        for i in range(steps + 1):
            progress = i / steps
            filled = int(width * progress)
            
            bar_chars = []
            for j in range(filled):
                color = colors[j % len(colors)]
                bar_chars.append(f"{color}█{Colors.RESET}")
            
            for j in range(width - filled):
                bar_chars.append(f"{Colors.DIM}░{Colors.RESET}")
            
            bar = "".join(bar_chars)
            percent = int(progress * 100)
            
            elapsed = time.time() - start
            if progress > 0:
                eta = (elapsed / progress) - elapsed
                eta_str = f"{eta:.1f}s"
            else:
                eta_str = "--.-s"
            
            sys.stdout.write(
                f'\r{Colors.CYAN}[{Colors.B_CYAN}●{Colors.RESET}{Colors.CYAN}]{Colors.RESET} '
                f'{bar} {Colors.YELLOW}{percent:3d}%{Colors.RESET} '
                f'{Colors.BLUE}ETA: {eta_str}{Colors.RESET}'
            )
            sys.stdout.flush()
            time.sleep(duration / (steps + 1))
        
        print()

# ============================================================================
# SMART SUGGESTION ENGINE
# ============================================================================

class SuggestionEngine:
    """Smart command suggestion system"""
    
    ALL_COMMANDS = [
        "--help", "--version", "help", "version", "doctor",
        "target-set", "target-show", "target-clear", "target-ping",
        "proxy-start", "proxy-stop", "proxy-status", "proxy-config",
        "capture-start", "capture-stop", "capture-list", "capture-clear",
        "flow-analyze", "flow-show", "flow-export", "flow-reset",
        "logic-test", "logic-rules", "logic-enable", "logic-disable",
        "session-analyze", "session-reuse-test", "session-invalidate-test",
        "diff-run", "diff-summary",
        "report-generate", "report-show", "report-export",
        "clear", "exit"
    ]
    
    @staticmethod
    def get_suggestions(user_input, num_suggestions=3):
        """Get command suggestions based on similarity"""
        user_cmd = user_input.strip().lower()
        
        # Find close matches
        close_matches = difflib.get_close_matches(
            user_cmd,
            SuggestionEngine.ALL_COMMANDS,
            n=num_suggestions,
            cutoff=0.6
        )
        
        return close_matches
    
    @staticmethod
    def suggest(user_input):
        """Provide suggestions for typo or unknown command"""
        suggestions = SuggestionEngine.get_suggestions(user_input)
        
        if suggestions:
            print(f"\n{Colors.YELLOW}[?] Did you mean:{Colors.RESET}")
            for idx, suggestion in enumerate(suggestions, 1):
                if suggestion.startswith("--"):
                    print(f"    {idx}. {Colors.GREEN}fg {suggestion}{Colors.RESET}")
                else:
                    print(f"    {idx}. {Colors.GREEN}fg {suggestion}{Colors.RESET}")
            print()

# ============================================================================
# MAIN APPLICATION
# ============================================================================

class FlowGuard:
    """Advanced web application security testing tool"""
    
    def __init__(self):
        self.state = AppState()
        self.version = "1.0.0"
        self.developer = "Jagan Bhasker - Jb"
        self.dev_email = "jaganbhaskergurram@gmail.com"
        self.repo = "github.com/Jaganbhasker1122/flowguard"
        self.suggestion_engine = SuggestionEngine()
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system("cls" if os.name == "nt" else "clear")
    
    def animated_banner(self):
        """Display animated banner"""
        banner = """
    ███████╗██╗      ██████╗ ██╗    ██╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
    ██╔════╝██║     ██╔═══██╗██║    ██║██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
    █████╗  ██║     ██║   ██║██║ █╗ ██║██║  ███╗██║   ██║███████║██████╔╝██║  ██║
    ██╔══╝  ██║     ██║   ██║██║███╗██║██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
    ██║     ███████╗╚██████╔╝╚███╔███╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
    ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
        """
        self.clear_screen()
        print(f"\n{Colors.CYAN}{banner}{Colors.RESET}")
    
    def get_visible_length(self, text):
        """
        Calculate the number of visible characters, ignoring ANSI escape sequences
        More reliable version especially for PowerShell/Windows Terminal
        """
        length = 0
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i:i+2] == '\033[':
                # Skip the entire escape sequence
                end = text.find('m', i + 2)
                if end != -1:
                    i = end + 1
                    continue
                else:
                    # Broken escape sequence - treat as normal char
                    length += 1
                    i += 1
            else:
                length += 1
                i += 1
        return length
    
    def print_box(self, title, content, width=82):
        """Print colorful content without box outlines"""
        
        # Title line with decorative elements
        if title:
            title_colored = f"{Colors.B_MAGENTA}╞═══ {Colors.RESET}{Colors.B_CYAN}{title}{Colors.RESET}{Colors.B_MAGENTA} ═══╡{Colors.RESET}"
            print(f"\n{title_colored}\n")
        
        # Content lines with alternating colors
        for idx, line in enumerate(content):
            if self.get_visible_length(line) == 0:
                # Empty line - just print newline
                print()
            else:
                print(f"{line}")
        
        print()  # Final spacing

    def show_welcome_screen(self):
        """Display professional welcome screen"""
        self.animated_banner()
        
        print(f"{Colors.BOLD}{Colors.MAGENTA}»»» SECURE FLOW ANALYSIS. DEEP TESTING. COMPLETE COVERAGE «««{Colors.RESET}\n")
        
        # Tool Description
        description = [
            "",
            f"{Colors.B_CYAN}ADVANCED WEB APPLICATION SECURITY TESTING FRAMEWORK{Colors.RESET}",
            "",
            "FlowGuard is a professional-grade security testing tool designed for authorized",
            "penetration testers and security researchers. It provides comprehensive traffic",
            "analysis, HTTP flow detection, business logic testing, and session validation",
            "capabilities for identifying vulnerabilities in web applications.",
            "",
            f"{Colors.YELLOW}Key Capabilities:{Colors.RESET}",
            f"  {Colors.GREEN}✓{Colors.RESET} Real-time traffic capture and deep packet inspection",
            f"  {Colors.GREEN}✓{Colors.RESET} Intelligent HTTP request flow detection and visualization",
            f"  {Colors.GREEN}✓{Colors.RESET} Business logic vulnerability identification and testing",
            f"  {Colors.GREEN}✓{Colors.RESET} Session token lifecycle and entropy analysis",
            f"  {Colors.GREEN}✓{Colors.RESET} Advanced response comparison and anomaly detection",
            f"  {Colors.GREEN}✓{Colors.RESET} Comprehensive security assessment reporting",
            f"  {Colors.GREEN}✓{Colors.RESET} 40+ specialized testing commands and modules",
            "",
            f"{Colors.YELLOW}Professional Features:{Colors.RESET}",
            f"  {Colors.BLUE}→{Colors.RESET} Interactive terminal interface with real-time feedback",
            f"  {Colors.BLUE}→{Colors.RESET} Multiple export formats (JSON, XML, HTML)",
            f"  {Colors.BLUE}→{Colors.RESET} Customizable security rules and testing parameters",
            f"  {Colors.BLUE}→{Colors.RESET} Smart command suggestions for typos and mistakes",
            "",
        ]
        
        self.print_box("TOOL DESCRIPTION", description)
        
        # Tool Information
        info = [
            "",
            f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
            f"{Colors.YELLOW}Version:{Colors.RESET}          {Colors.GREEN}v{self.version}{Colors.RESET}",
            f"{Colors.YELLOW}Developer:{Colors.RESET}       {Colors.GREEN}{self.developer}{Colors.RESET}",
            f"{Colors.YELLOW}Email:{Colors.RESET}           {Colors.B_BLUE}{self.dev_email}{Colors.RESET}",
            f"{Colors.YELLOW}Repository:{Colors.RESET}      {Colors.B_BLUE}{self.repo}{Colors.RESET}",
            f"{Colors.YELLOW}Release Date:{Colors.RESET}    {Colors.GREEN}to be released soon..{Colors.RESET}",
            f"{Colors.YELLOW}Status:{Colors.RESET}         {Colors.GREEN}Testing...{Colors.RESET}",
            f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
            "",
            f"{Colors.B_RED}⚠  LEGAL DISCLAIMER:{Colors.RESET}",
            f"{Colors.RED}Authorized security testing only. Unauthorized access is illegal.{Colors.RESET}",
            f"{Colors.RED}Always obtain explicit permission. The developers assume no liability.{Colors.RESET}",
            "",
        ]
        
        self.print_box("TOOL INFORMATION", info)
    
    def initialization_sequence(self):
        """Initialize tool with progress bar"""
        print(f"\n{Colors.BOLD}{Colors.B_CYAN}[⚙] INITIALIZING FLOWGUARD v{self.version}{Colors.RESET}\n")
        
        ColorfulProgressBar.animate(
            duration=3.0,
            label="Loading modules, engines, and security signatures...",
            width=70
        )
        
        print()
        print(f"{Colors.GREEN}[+] System initialization complete{Colors.RESET}")
        print(f"{Colors.GREEN}[+] All modules loaded successfully{Colors.RESET}")
        print(f"{Colors.BLUE}[i] Type 'fg --help' for command reference{Colors.RESET}\n")
        
        self.state.initialized = True
    
    def show_help(self):
        """Display help with command categories"""
        help_text = [
            "",
            f"{Colors.B_CYAN}AVAILABLE COMMANDS{Colors.RESET}",
            "",
            f"{Colors.YELLOW}Target Management:{Colors.RESET}",
            f"  {Colors.GREEN}fg target-set --url <URL>{Colors.RESET}     Set target URL for testing",
            f"  {Colors.GREEN}fg target-show{Colors.RESET}                Display current target",
            f"  {Colors.GREEN}fg target-clear{Colors.RESET}               Clear target configuration",
            f"  {Colors.GREEN}fg target-ping{Colors.RESET}                Check target reachability",
            "",
            f"{Colors.YELLOW}Proxy Control:{Colors.RESET}",
            f"  {Colors.CYAN}fg proxy-start{Colors.RESET}                Start proxy on 127.0.0.1:8080",
            f"  {Colors.CYAN}fg proxy-stop{Colors.RESET}                 Stop running proxy",
            f"  {Colors.CYAN}fg proxy-status{Colors.RESET}               Show proxy status",
            f"  {Colors.CYAN}fg proxy-config{Colors.RESET}               Display proxy settings",
            "",
            f"{Colors.YELLOW}Traffic Capture:{Colors.RESET}",
            f"  {Colors.MAGENTA}fg capture-start{Colors.RESET}              Begin traffic capture",
            f"  {Colors.MAGENTA}fg capture-stop{Colors.RESET}               Stop traffic capture",
            f"  {Colors.MAGENTA}fg capture-list{Colors.RESET}               Display captured requests",
            f"  {Colors.MAGENTA}fg capture-clear{Colors.RESET}              Clear captured data",
            "",
            f"{Colors.YELLOW}Flow Analysis:{Colors.RESET}",
            f"  {Colors.B_GREEN}fg flow-analyze{Colors.RESET}               Analyze HTTP request flows",
            f"  {Colors.B_GREEN}fg flow-show{Colors.RESET}                  Display detected flows",
            f"  {Colors.B_GREEN}fg flow-export --format json{Colors.RESET}  Export flows",
            f"  {Colors.B_GREEN}fg flow-reset{Colors.RESET}                 Reset flow analysis",
            "",
            f"{Colors.YELLOW}Business Logic Testing:{Colors.RESET}",
            f"  {Colors.B_RED}fg logic-test{Colors.RESET}                 Run logic vulnerability tests",
            f"  {Colors.B_RED}fg logic-rules{Colors.RESET}                List security rules",
            f"  {Colors.B_RED}fg logic-enable --rule <n>{Colors.RESET}    Enable specific rule",
            f"  {Colors.B_RED}fg logic-disable --rule <n>{Colors.RESET}   Disable specific rule",
            "",
            f"{Colors.YELLOW}Session Validation:{Colors.RESET}",
            f"  {Colors.B_YELLOW}fg session-analyze{Colors.RESET}            Analyze session tokens",
            f"  {Colors.B_YELLOW}fg session-reuse-test{Colors.RESET}         Test token reuse",
            f"  {Colors.B_YELLOW}fg session-invalidate-test{Colors.RESET}    Test session termination",
            "",
            f"{Colors.YELLOW}Response Comparison:{Colors.RESET}",
            f"  {Colors.B_CYAN}fg diff-run --req-a 1 --req-b 2{Colors.RESET}  Compare responses",
            f"  {Colors.B_CYAN}fg diff-summary{Colors.RESET}                Show comparison summary",
            "",
            f"{Colors.YELLOW}Reporting:{Colors.RESET}",
            f"  {Colors.B_MAGENTA}fg report-generate{Colors.RESET}            Generate security report",
            f"  {Colors.B_MAGENTA}fg report-show{Colors.RESET}                Display current report",
            f"  {Colors.B_MAGENTA}fg report-export --format html{Colors.RESET} Export report",
            "",
            f"{Colors.YELLOW}Utility:{Colors.RESET}",
            f"  {Colors.BLUE}fg doctor{Colors.RESET}                     Check system readiness",
            f"  {Colors.BLUE}fg --version{Colors.RESET}                  Show version information",
            f"  {Colors.BLUE}fg --help{Colors.RESET}                     Display this help message",
            f"  {Colors.BLUE}fg clear{Colors.RESET}                      Clear terminal screen",
            f"  {Colors.BLUE}fg exit{Colors.RESET}                       Exit the application",
            "",
        ]
        
        self.print_box("COMMAND REFERENCE", help_text)
    
    def show_version(self):
        """Display version information"""
        info = [
            "",
            f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
            f"{Colors.YELLOW}Application:{Colors.RESET}    {Colors.GREEN}FlowGuard{Colors.RESET}",
            f"{Colors.YELLOW}Version:{Colors.RESET}        {Colors.GREEN}v{self.version}{Colors.RESET}",
            f"{Colors.YELLOW}Status:{Colors.RESET}         {Colors.GREEN}Production Ready{Colors.RESET}",
            f"{Colors.YELLOW}Release Date:{Colors.RESET}    {Colors.GREEN}January 15, 2025{Colors.RESET}",
            f"{Colors.YELLOW}Developer:{Colors.RESET}       {Colors.B_GREEN}{self.developer}{Colors.RESET}",
            f"{Colors.YELLOW}Email:{Colors.RESET}          {Colors.B_CYAN}{self.dev_email}{Colors.RESET}",
            f"{Colors.YELLOW}Repository:{Colors.RESET}     {Colors.B_BLUE}{self.repo}{Colors.RESET}",
            f"{Colors.YELLOW}License:{Colors.RESET}       {Colors.GREEN}MIT License{Colors.RESET}",
            f"{Colors.B_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}",
            "",
        ]
        
        self.print_box("VERSION INFORMATION", info)
    
    
    
   
    
    def execute_command(self, cmd_parts):
        """Execute command"""
        if not cmd_parts:
            return
        
        # Handle 'fg' prefix if present
        if cmd_parts[0].lower() == "fg" and len(cmd_parts) > 1:
            cmd_parts = cmd_parts[1:]
        
        if not cmd_parts:
            return
        
        cmd = cmd_parts[0]
        
        # Command routing
        commands = {
            "--help": self.show_help,
            "help": self.show_help,
            "--version": self.show_version,
            "version": self.show_version,
            "doctor": lambda: run_doctor(self.state, Colors),
            "target-set": lambda: target_set(self.state, cmd_parts, Colors, ColorfulProgressBar),
            "target-show": lambda: target_show(self.state, Colors, self.print_box),
            "target-clear": lambda: target_clear(self.state, Colors),
            "target-ping": lambda: target_ping(self.state, Colors, ColorfulProgressBar),
            "proxy-start": lambda: proxy_start(self.state, Colors, ColorfulProgressBar),
            "proxy-stop": lambda: proxy_stop(self.state, Colors, ColorfulProgressBar),
            "proxy-status": lambda: proxy_status(self.state, Colors, self.print_box),
            "proxy-config": lambda: proxy_config(Colors, self.print_box),
            "capture-start": lambda: capture_start(self.state, Colors, ColorfulProgressBar),
            "capture-stop": lambda: capture_stop(self.state, Colors, ColorfulProgressBar),
            "capture-list": lambda: capture_list(self.state, Colors, ColorfulProgressBar, self.print_box),
            "capture-clear": lambda: capture_clear(self.state, Colors, ColorfulProgressBar),
            "flow-analyze": lambda: flow_analyze(self.state, Colors, ColorfulProgressBar),
            "flow-show": lambda: flow_show(self.state, Colors, ColorfulProgressBar, self.print_box),
            "flow-export": lambda: flow_export(self.state, cmd_parts, Colors, ColorfulProgressBar),
            "flow-reset": lambda: flow_reset(self.state, Colors, ColorfulProgressBar),
            "logic-test": lambda: logic_test(self.state, Colors),
            "logic-rules": lambda: logic_rules(self.state, Colors, self.print_box),
            "logic-enable": lambda: logic_enable(self.state, cmd_parts, Colors),
            "logic-disable": lambda: logic_disable(self.state, cmd_parts, Colors),
            "session-analyze": lambda: session_analyze(self.state, Colors, ColorfulProgressBar),
            "session-reuse-test": lambda: session_reuse_test(self.state, Colors, ColorfulProgressBar),
            "session-invalidate-test": lambda: session_invalidate_test(self.state, Colors, ColorfulProgressBar),
            "diff-run": lambda: diff_run(self.state, cmd_parts, Colors, ColorfulProgressBar, self.print_box),
            "diff-summary": lambda: diff_summary(self.state, Colors, ColorfulProgressBar, self.print_box),
            "report-generate": lambda: report_generate(self.state, Colors, ColorfulProgressBar),
            "report-show": lambda: report_show(self.state, Colors, self.print_box),
            "report-export": lambda: report_export(self.state, cmd_parts, Colors, ColorfulProgressBar),


            "clear": self.clear_screen,
        }
        
        if cmd in commands:
            commands[cmd]()
        else:
            print(f"\n{Colors.RED}[!] Unknown command: '{cmd}'{Colors.RESET}")
            # Provide smart suggestions
            self.suggestion_engine.suggest(cmd)
            print(f"{Colors.YELLOW}[?] Type 'fg --help' for available commands{Colors.RESET}\n")
    
    def run_shell(self):
        """Run interactive shell"""
        self.show_welcome_screen()
        self.initialization_sequence()
        
        while True:
            try:
                prompt = f"{Colors.BOLD}{Colors.MAGENTA}flowguard{Colors.RESET}{Colors.CYAN}>{Colors.RESET} "
                user_input = input(prompt).strip()
                
                if user_input.lower() == "exit" or user_input.lower() == "fg exit":
                    print(f"\n{Colors.YELLOW}[!] Exiting FlowGuard{Colors.RESET}")
                    print(f"{Colors.GREEN}[+] Goodbye!{Colors.RESET}\n")
                    break
                
                if not user_input:
                    continue
                
                cmd_parts = user_input.split()
                self.execute_command(cmd_parts)
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}[!] Interrupted by user{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Goodbye!{Colors.RESET}\n")
                break
            except Exception as e:
                print(f"\n{Colors.RED}[ERROR] {e}{Colors.RESET}\n")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point"""
    try:
        app = FlowGuard()
        app.run_shell()
    except Exception as e:
        print(f"{Colors.RED}[FATAL] {e}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()