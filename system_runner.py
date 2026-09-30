"""
D3M13N-CAPSULECRAFT: Unified System Runner
Integrates BCI Telemetry Engine and Broker Compartment Injunction (BCI)
into a complete end-to-end pipeline check.
"""

import hmac
import hashlib
import json
from bci_telemetry_engine import BCITelemetryEngine
from broker_compartment_injunction import BrokerCompartmentInjunction

def run_pipeline():
    print("=== INITIALIZING D3M13N-CAPSULECRAFT UNIFIED PIPELINE ===")
    
    # 1. Initialize Modules
    secret = "CAPSULECRAFT-UNIFIED-KEY"
    broker = BrokerCompartmentInjunction(master_secret=secret)
    telemetry_engine = BCITelemetryEngine(node_id="UNIFIED-BCI-01")
    
    node_id = "COMPUTE-NODE-OMEGA"
    signature = "sig_omega_99"
    
    print(f"[+] Registering node-lock for {node_id}...")
    broker.register_node_lock(node_id, signature)
    
    # Generate valid token for simulation
    token = hmac.new(secret.encode("utf-8"), f"{node_id}:{signature}".encode("utf-8"), hashlib.sha256).hexdigest()
    
    # 2. Execute Broker Injunction & Routing Check
    sample_payload = {"positive_val": 5.2, "negative_val": 1.1}
    print(f"[+] Routing packet through Broker Compartment Injunction...")
    routing_result = broker.verify_and_route_packet(node_id, token, sample_payload)
    print(json.dumps(routing_result, indent=2))
    
    if routing_result["status"] == "ROUTED_SECURE":
        print(f"[+] Routing successful. Passing telemetry to BCI Telemetry Engine...")
        sweep_result = telemetry_engine.execute_radius_sweep(sample_payload)
        print(json.dumps(sweep_result, indent=2))
        print("=== PIPELINE CHECK COMPLETED SUCCESSFULLY ===")
        return True
    else:
        print("[-] Pipeline halted due to routing injunction failure.")
        return False

if __name__ == "__main__":
    run_pipeline()
