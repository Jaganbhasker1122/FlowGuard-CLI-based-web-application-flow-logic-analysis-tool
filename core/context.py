
# ============================================================================
# APP STATE
# ============================================================================

class AppState:
    """Application state management"""
    
    def __init__(self):
        self.target_url = None
        self.proxy_running = False
        self.capture_running = False
        self.captured_requests = []
        self.flows = []
        self.current_report = None
        self.initialized = False
        self.session_tokens = ["token_abc123", "token_def456", "token_ghi789"]
        self.logic_rules = {
            "admin_bypass": True,
            "privilege_escalation": True,
            "parameter_tampering": True,
            "session_fixation": True,
            "insecure_direct_refs": True,
        }
