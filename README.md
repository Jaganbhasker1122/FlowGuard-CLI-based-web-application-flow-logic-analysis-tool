# FlowGuard

A CLI-based security analysis tool for identifying logic flaws and access control weaknesses in web application workflows.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen)]()

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [What is FlowGuard](#what-is-flowguard)
3. [Key Features](#key-features)
4. [Quick Start](#quick-start)
5. [CLI Commands](#cli-commands)
6. [Architecture](#architecture)
7. [How It Works](#how-it-works)
8. [Use Cases](#use-cases)
9. [Limitations](#limitations)
10. [Future Roadmap](#future-roadmap)
11. [Contributing](#contributing)
12. [License](#license)
13. [Author](#author)

---

## Problem Statement

Traditional web application security testing focuses on individual endpoints—testing each URL for input validation, SQL injection, XSS, and other common vulnerabilities. However, many real-world vulnerabilities emerge from **application logic and state management**, not from weak input handling.

**Common logic-based vulnerabilities include:**

- **Skipped Steps**: Accessing protected workflows without completing prerequisite steps (e.g., checkout without payment)
- **Session Reuse**: Using expired or invalidated sessions to maintain unauthorized access
- **Privilege Escalation**: Accessing higher-privilege features by manipulating request sequences
- **State Confusion**: Exploiting transitions between application states to bypass authorization
- **Authorization Inconsistencies**: Different access rules applied across alternate paths to the same resource

Traditional security scanners miss these issues because they test endpoints in isolation. FlowGuard addresses this gap by analyzing **multi-step application behavior and state transitions**.

---

## What is FlowGuard

FlowGuard is a simulation-driven security analysis tool that identifies logic flaws by examining how web applications handle sequences of requests, session management, and state transitions. Instead of testing individual endpoints, FlowGuard simulates realistic user workflows and detects abnormal behavior patterns.

**Key insight:** Security issues frequently stem from broken logic, not broken syntax. FlowGuard focuses on application flows and state transitions to uncover vulnerabilities that endpoint-only testing overlooks.

---

## Key Features

### Target Management
- Set and manage target application URLs
- Validate target reachability
- Quick configuration and context switching

### Proxy Control
- Start, stop, and monitor proxy engine (simulation mode)
- Foundation for traffic interception workflows
- Designed for future live proxy integration

### Traffic Capture
- Begin and stop traffic capture sessions
- Inspect and list captured request data
- Clear captured data for fresh analyses
- Input foundation for flow analysis

### Flow Analysis
- Detect skipped steps in application workflows
- Identify abnormal navigation and state transitions
- View discovered flows in structured format
- Export flow data for reporting and external analysis

### Logic Rule Engine
- Built-in detection rules: admin bypass, session fixation, privilege escalation
- Enable and disable rules dynamically
- Run comprehensive logic tests against captured flows
- Extensible architecture for custom rules

### Session Analysis
- Analyze session lifecycle and usage patterns
- Test for session reuse vulnerabilities
- Validate session invalidation behavior
- Detect token handling issues

### Diff Analysis
- Compare application behavior between versions
- Identify changes in logic and authorization rules
- Generate summaries of behavioral differences
- Track security regressions

### Reporting
- Generate consolidated security analysis reports
- Export reports in multiple formats
- View results directly in CLI
- Suitable for compliance and audit documentation

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Jaganbhasker1122/flowguard.git
cd flowguard

# Install dependencies
pip install -r requirements.txt

# Verify installation
python main.py --version
```

### Basic Workflow

```bash
# Start FlowGuard interactive CLI
python main.py

# Set your target application
fg target-set --url https://demo-app.local

# Begin security analysis
fg proxy-start
fg capture-start

# Analyze application flows
fg flow-analyze
fg logic-test

# Generate report
fg report-generate
fg report-show
```

---

## CLI Commands

All FlowGuard commands are prefixed with `fg`.

### General Commands

| Command | Description |
|---------|-------------|
| `fg help` | Display all available commands and options |
| `fg version` | Show FlowGuard version information |
| `fg doctor` | Run system and configuration health check |
| `fg clear` | Clear the terminal screen |

### Target Management

| Command | Description |
|---------|-------------|
| `fg target-set --url <URL>` | Set the target application URL |
| `fg target-show` | Display current target configuration |
| `fg target-clear` | Clear the target configuration |
| `fg target-ping` | Validate target reachability |

### Proxy Control (Simulation Mode)

| Command | Description |
|---------|-------------|
| `fg proxy-start` | Start the proxy engine |
| `fg proxy-stop` | Stop the running proxy |
| `fg proxy-status` | Display current proxy status |
| `fg proxy-config` | Show proxy configuration details |

### Traffic Capture (Simulation Mode)

| Command | Description |
|---------|-------------|
| `fg capture-start` | Begin traffic capture session |
| `fg capture-stop` | Stop traffic capture |
| `fg capture-list` | List captured requests |
| `fg capture-clear` | Clear all captured data |

### Flow Analysis

| Command | Description |
|---------|-------------|
| `fg flow-analyze` | Analyze captured flows for logic issues |
| `fg flow-show` | Display discovered application flows |
| `fg flow-export` | Export flow data (JSON/CSV) |
| `fg flow-reset` | Clear all flow analysis data |

### Logic Rule Engine

| Command | Description |
|---------|-------------|
| `fg logic-test` | Run logic tests against flows |
| `fg logic-rules` | Display available detection rules |
| `fg logic-enable <rule>` | Enable a specific rule |
| `fg logic-disable <rule>` | Disable a specific rule |

### Session Analysis

| Command | Description |
|---------|-------------|
| `fg session-analyze` | Analyze session patterns and lifecycle |
| `fg session-reuse-test` | Test for session reuse vulnerabilities |
| `fg session-invalidate-test` | Test session invalidation behavior |

### Diff Analysis

| Command | Description |
|---------|-------------|
| `fg diff-run --baseline <v1> --compare <v2>` | Compare behavior between versions |
| `fg diff-summary` | Display summary of differences |

### Reporting

| Command | Description |
|---------|-------------|
| `fg report-generate` | Generate security analysis report |
| `fg report-show` | Display the generated report |
| `fg report-export --format <format>` | Export report in specified format |

---

## Architecture

### Project Structure

```
flowguard/
├── main.py                 # CLI entry point and command router
├── core/                   # Core application state management
│   ├── app_state.py       # Shared state across modules
│   └── command_router.py  # Command parsing and routing
├── modules/               # Feature modules (isolated and independent)
│   ├── target.py          # Target management
│   ├── proxy.py           # Proxy lifecycle control
│   ├── capture.py         # Traffic capture engine
│   ├── flow.py            # Flow analysis and detection
│   ├── logic.py           # Logic rule engine
│   ├── session.py         # Session analysis
│   ├── diff.py            # Version comparison
│   └── report.py          # Report generation
├── utils/                 # Shared utilities
│   ├── ui.py              # Terminal UI helpers
│   ├── validation.py      # Input validation
│   └── formatters.py      # Output formatting
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

### Design Principles

**Flow-First Security:** Analyzes multi-step behaviors and state transitions rather than individual endpoints.

**State-Aware Analysis:** Tracks session state, authorization context, and sequence dependencies across requests.

**CLI-Driven:** Transparent, scriptable, and easily automatable interface for integration into security workflows.

**Simulation-Based:** Deterministic testing without environment dependencies, enabling consistent and repeatable analysis.

**Modular Design:** Isolated modules with clear interfaces, designed for extensibility and maintenance.

---

## How It Works

### Analysis Pipeline

1. **Target Configuration**: Set the target application URL and configuration
2. **Proxy Start**: Initialize the analysis engine
3. **Traffic Capture**: Capture or simulate application traffic
4. **Flow Analysis**: Detect request sequences, state transitions, and abnormal patterns
5. **Logic Testing**: Run detection rules to identify vulnerabilities
6. **Session Analysis**: Analyze session management and lifecycle
7. **Report Generation**: Compile findings into a security report

### Example: Detecting Skipped Steps

**Scenario:** A web application requires users to complete a multi-step checkout process:
1. Select items (cart)
2. Enter shipping address
3. Confirm payment
4. Place order

**FlowGuard detects:** A user accessing step 4 (place order) without completing step 3 (confirm payment).

**Detection:** This represents a skipped step vulnerability—a logic flaw that allows order placement without payment processing.

### Execution Mode

FlowGuard operates in **Simulation Mode**, generating realistic application flows and traffic synthetically. This approach:

- Enables full end-to-end testing without external dependencies
- Produces deterministic and repeatable results
- Simplifies cross-platform compatibility
- Avoids OS-level proxy complexity

Simulation mode is ideal for learning, validation, and integration testing.

---

## Use Cases

### Security Testing and Validation

Identify logic flaws in multi-step workflows, validate authorization rules across alternate paths, and test session management behavior without requiring access to a live application.

### Regression Testing

Compare security behavior across application versions to detect unintended changes in access control logic or behavioral differences that might introduce new vulnerabilities.

### Educational and Demonstrations

Teach logic-based vulnerability concepts, demonstrate how flow analysis detects complex vulnerabilities, and validate security logic before implementation.

### Compliance and Audit

Generate detailed security analysis reports, document application flow behavior, and provide evidence of comprehensive security testing for compliance requirements.

---

## Limitations

The following are intentional design choices reflecting the project scope:

**Execution Mode:**
- Operates in simulation mode; live HTTP/HTTPS interception not enabled
- Traffic data is synthetically generated, not captured from real browsers
- Designed for logic validation rather than production proxy functionality

**Interface and Configuration:**
- CLI-only interface (no GUI)
- Rules are predefined; custom rule configuration files planned for future release
- Report formats currently text and basic structured output

**Analysis Scope:**
- Focuses on application logic and flow; does not perform input validation testing
- Does not include vulnerability payloads (e.g., XSS, SQL injection)
- Targets web application workflows, not infrastructure or network security

These constraints keep the focus on logic correctness and cross-platform compatibility while maintaining a clear project scope.

---

## Future Roadmap

### Short-term Enhancements
- Live HTTP/HTTPS traffic interception (Linux/WSL support)
- Support for multiple data sources (proxy logs, PCAP files, HAR exports)
- Custom rule framework with configuration file support

### Medium-term Improvements
- Interactive flow visualization and dependency graphs
- CI/CD pipeline integration for automated regression testing
- Enhanced reporting (PDF export, HTML dashboards, compliance templates)

### Long-term Vision
- Machine learning-based anomaly detection
- Behavioral baseline learning from normal traffic
- Integration with other security tools and frameworks

---

## Contributing

Contributions are welcome. Areas for contribution include:

- New detection rules and logic patterns
- Enhanced reporting formats and export options
- Documentation, examples, and tutorials
- Bug reports and feature requests
- Platform-specific improvements

**To contribute:**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/description`)
3. Commit your changes with clear messages
4. Push to the branch and open a pull request

Please include test cases and documentation with your contributions.

---

## License

FlowGuard is released under the MIT License. See the LICENSE file for details.

---

## Author

**Gurram Jagan Bhasker**  
B.Tech Cyber Security (3rd Year) | India

Cybersecurity professional with expertise in application security, logic flaw analysis, and defensive security tooling. Focused on building practical, research-oriented security projects.

### Contact and Profiles

- GitHub: [github.com/Jaganbhasker1122](https://github.com/Jaganbhasker1122)
- LinkedIn: [linkedin.com/in/gurram-jagan-bhasker-a0906b29a](https://www.linkedin.com/in/gurram-jagan-bhasker-a0906b29a/)
- Email: jaganbhaskergurram@gmail.com

---

*FlowGuard: Where logic meets security.*
