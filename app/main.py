import argparse
from app import create_app

def print_banner():
    banner = """
   ____                   _    _             _ _   
  / __ \                 | |  | |           | | |  
 | |  | |_ __   ___ _ __ | |  | | __ _ _   _| | |_ 
 | |  | | '_ \ / _ \ '_ \| |  | |/ _` | | | | | __|
 | |__| | |_) |  __/ | | \ \_/ / (_| | |_| | | |_ 
  \____/| .__/ \___|_| |_|\___/ \__,_|\__,_|_|\__|
        | |                                        
        |_|       v0.4.0 (Student Edition)         
    """
    print(banner)

def main():
    parser = argparse.ArgumentParser(description="Run the OpenVault server")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on")
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode")

    args = parser.parse_args()
    print_banner()
    print(f"[*] Starting OpenVault on http://{args.host}:{args.port}")
    print("[*] (Please do not use master password '123456')")

    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()
