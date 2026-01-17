# FlowGuard

> **Advanced Security Analysis for Web Application Logic and Flow**

A CLI-based security analysis tool designed to identify and analyze complex vulnerabilities in web applications through simulation-driven flow logic testing. FlowGuard examines session behavior, access control weaknesses, and state transitions that traditional endpoint-only testing misses.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen)](https://github.com/)

---

## 🎯 Overview

Modern web vulnerabilities frequently stem from **logic and flow issues** rather than input validation defects. FlowGuard addresses this gap by providing a structured, simulation-driven approach to discovering:

- **Skipped Steps**: Accessing protected workflows without completing prerequisite steps
- **Session Vulnerabilities**: Expired session reuse, session fixation, and validation bypasses
- **Access Control Flaws**: Role-based authorization inconsistencies across alternate paths
- **Behavioral Anomalies**: Unexpected differences in application logic between versions

### Why FlowGuard?

Traditional security tools focus on individual endpoints. FlowGuard observes **multi-step application behavior**, state transitions, and sequence dependencies to uncover logic-based vulnerabilities that scanners miss.

---

## ✨ Key Features

### 🔹 Target Management
- Set, view, and ping target applications
- Centralized context for all security analyses
- Quick target validation and reachability checks

### 🌐 Proxy Control (Simulated)
- Start, stop, and monitor proxy engine lifecycle
- Designed to mirror real HTTP interception workflows
- Foundation for future live proxy integration

### 📥 Traffic Capture (Simulated)
- Begin and stop traffic capture sessions
- List and inspect captured request data
- Clear captured traffic for fresh analyses
- Input foundation for flow analysis engine

### 🔀 Flow Analysis
- Analyze request sequences and state transitions
- Detect skipped steps and abnormal navigation patterns
- View discovered application flows in structured format
- Export flow data for external inspection and reporting

### 🧠 Logic Rule Engine
- Built-in rules: admin bypass, session fixation, privilege escalation
- Dynamic rule enable/disable functionality
- Run comprehensive logic tests against captured flows
- Extensible architecture for custom rule development

### 🔐 Session Analysis
- Analyze session usage patterns and lifecycle
- Detect session reuse vulnerabilities
- Test session invalidation behavior
- Validate session expiration and token handling

### 🔍 Diff Analysis
- Compare application behavior between versions
- Identify changes in flow logic and authorization rules
- Generate detailed summaries of behavioral differences
- Track security regression testing

### 📊 Reporting
- Generate consolidated security analysis reports
- View results directly in CLI interface
- Export reports in supported formats
- Structured output suitable for compliance and audit

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/flowguard.git
cd flowguard

# Install dependencies
pip install -r requirements.txt

# Verify installation
python main.py --version
```

### Basic Usage

```bash
# Start FlowGuard
python main.py

# Set your target application
fg target-set --url https://demo-app.local

# Start the proxy and begin analysis
fg proxy-start
fg capture-start

# Analyze flows
fg flow-analyze
fg report-generate

# View results
fg report-show
```

---

## 📖 Command Reference

All FlowGuard commands are prefixed with `fg`.

### General Commands

| Command | Description |
|---------|-------------|
| `fg --help` / `fg help` | Display all available commands and usage |
| `fg --version` / `fg version` | Show FlowGuard version information |
| `fg doctor` | Run system and configuration health check |
| `fg clear` | Clear the terminal screen |

### Target Management

| Command | Description |
|---------|-------------|
| `fg target-set --url <URL>` | Set the target application URL |
| `fg target-show` | Display the currently configured target |
| `fg target-clear` | Clear the current target configuration |
| `fg target-ping` | Check target reachability (simulated) |

### Proxy Control (Simulated)

| Command | Description |
|---------|-------------|
| `fg proxy-start` | Start the proxy engine (simulation mode) |
| `fg proxy-stop` | Stop the running proxy |
| `fg proxy-status` | Show current proxy status |
| `fg proxy-config` | Display proxy configuration details |

### Traffic Capture (Simulated)

| Command | Description |
|---------|-------------|
| `fg capture-start` | Begin traffic capture |
| `fg capture-stop` | Stop traffic capture |
| `fg capture-list` | List captured requests |
| `fg capture-clear` | Clear all captured traffic data |

### Flow Analysis

| Command | Description |
|---------|-------------|
| `fg flow-analyze` | Analyze captured flows for logic issues |
| `fg flow-show` | Display discovered application flows |
| `fg flow-export` | Export flow data (JSON/CSV format) |
| `fg flow-reset` | Clear all flow analysis data |

### Logic Engine

| Command | Description |
|---------|-------------|
| `fg logic-test` | Run logic tests against analyzed flows |
| `fg logic-rules` | Display available logic rules |
| `fg logic-enable <rule>` | Enable a specific logic rule |
| `fg logic-disable <rule>` | Disable a specific logic rule |

### Session Analysis

| Command | Description |
|---------|-------------|
| `fg session-analyze` | Analyze session usage patterns |
| `fg session-reuse-test` | Test for session reuse vulnerabilities |
| `fg session-invalidate-test` | Test session invalidation behavior |

### Diff Analysis

| Command | Description |
|---------|-------------|
| `fg diff-run --baseline <v1> --compare <v2>` | Compare application behavior between versions |
| `fg diff-summary` | Display summary of detected differences |

### Reporting

| Command | Description |
|---------|-------------|
| `fg report-generate` | Generate a comprehensive security analysis report |
| `fg report-show` | Display the generated report |
| `fg report-export --format <format>` | Export report in specified format |

---

## 🏗️ Architecture

### Project Structure

```
flowguard/
├── main.py                 # CLI entry point and command router
├── core/                   # Core application state and engine
│   ├── app_state.py       # Shared application state management
│   └── command_router.py  # Command parsing and routing
├── modules/               # Feature modules (fully isolated)
│   ├── target.py          # Target management
│   ├── proxy.py           # Proxy lifecycle control
│   ├── capture.py         # Traffic capture engine
│   ├── flow.py            # Flow analysis module
│   ├── logic.py           # Logic rule engine
│   ├── session.py         # Session analysis
│   ├── diff.py            # Version comparison
│   └── report.py          # Report generation
├── utils/                 # Shared utilities
│   ├── ui.py              # Terminal UI helpers
│   ├── validation.py      # Input validation
│   └── formatters.py      # Output formatting
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

### Design Philosophy

- **Flow-First Security**: Analyzes multi-step behaviors, not just individual endpoints
- **State-Aware Analysis**: Tracks sessions, transitions, and sequence dependencies
- **CLI-Driven**: Transparent, automatable, and scriptable interface
- **Simulation-Based**: Deterministic testing without environment dependencies
- **Modular Design**: Isolated modules with clear interfaces for extensibility

---

## 🧪 Testing & Validation

All FlowGuard commands have been manually tested end-to-end using the simulation engine.

**Test Coverage Includes:**
- Target setup and configuration management
- Proxy lifecycle (start, stop, status)
- Traffic capture (start, stop, list, clear)
- Flow analysis and export functionality
- Logic rule testing and management
- Session analysis and vulnerability detection
- Diff analysis and version comparison
- Report generation and export

**Validation Results:**
✅ No command crashes or state inconsistencies  
✅ Deterministic and repeatable results  
✅ Proper error handling and user feedback  

---

## 🛠️ Current Execution Mode

### Simulation Mode (Stable)

FlowGuard operates in **Simulation Mode**, generating realistic web traffic, sessions, and application flows synthetically. This approach enables:

- Full end-to-end testing of logic without environment dependencies
- Deterministic and repeatable security analyses
- Easy demonstrations, testing, and documentation
- Clean validation of security logic

**Why Simulation?**
- Avoids complexity of OS-level proxy interception
- Enables cross-platform compatibility
- Supports deterministic security testing
- Ideal for logic validation and educational use

---

## 🔮 Roadmap

### Planned Enhancements

- **Live Proxy Integration**: Real HTTP/HTTPS traffic interception (WSL/Linux)
- **Multiple Data Sources**: Support for proxy logs, PCAP files, HAR exports
- **Graph Visualization**: Interactive flow visualization and dependency graphs
- **Custom Rule Framework**: Configuration file-based rule customization
- **CI/CD Integration**: Automated scenario testing and regression detection
- **Enhanced Reporting**: PDF export, HTML dashboards, compliance templates

---

## 📋 Current Limitations

The following limitations are intentional design choices:

- Live HTTP/HTTPS interception not enabled (use Simulation Mode)
- Traffic data is synthetically generated, not captured from real browsers
- CLI-only interface (no GUI)
- Rules are predefined (custom rules planned)

These constraints keep the focus on logic correctness and cross-platform compatibility rather than environment-specific complexities.

---

## 💡 Use Cases

### Security Testing & Validation
- Identify logic flaws in multi-step workflows
- Validate authorization across alternate paths
- Test session handling and expiration

### Regression Testing
- Compare security behavior across application versions
- Detect unintended changes in access control logic
- Track security improvements over time

### Educational & Demonstrations
- Teach security concepts around logic flaws
- Demonstrate flow-based vulnerability discovery
- Validate security logic before implementation

### Compliance & Audit
- Generate detailed security analysis reports
- Document application flow behavior
- Provide evidence of security testing

---

## 🤝 Contributing

Contributions are welcome! Areas for contribution:

- New logic rules and detection patterns
- Enhanced reporting formats
- Documentation and examples
- Bug reports and feature requests

Please submit issues and pull requests on GitHub.

---

## 📜 License

FlowGuard is released under the [MIT License](LICENSE).

---

## 🎓 Key Takeaway

**Security issues frequently emerge from broken logic, not broken syntax.** By focusing on application flows, session management, and state transitions, FlowGuard provides a foundation for next-generation application security analysis—addressing vulnerabilities that traditional endpoint-only testing overlooks.

---

## 📧 Support

For issues, questions, or feature requests:
- **Issues**: [GitHub Issues](https://github.com/yourusername/flowguard/issues)
- **Documentation**: See `docs/` directory for detailed guides
- **Examples**: Check `examples/` for workflow demonstrations

---

**FlowGuard**: *Where logic meets security.*

---

## 👤 Author

**Gurram Jagan Bhasker**  
B.Tech (3rd Year) – Cyber Security | India

Cybersecurity enthusiast with a strong interest in application security, logic flaw analysis, and defensive tooling. Focused on building practical, research-oriented security projects with expertise in malware analysis, threat hunting, and secure application design.

### 📫 Contact & Profiles

- **GitHub**: [github.com/Jaganbhasker1122](https://github.com/Jaganbhasker1122)
- **LinkedIn**: [linkedin.com/in/gurram-jagan-bhasker-a0906b29a](https://www.linkedin.com/in/gurram-jagan-bhasker-a0906b29a/)
- **Email**: [jaganbhaskergurram@gmail.com](mailto:jaganbhaskergurram@gmail.com)

---

*Built with ❤️ for the security community*
