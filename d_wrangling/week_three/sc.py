import socket
import struct
import time

# Magic handshake seen in PCAPs (example: 0x54097c0a)
HANDSHAKE_MAGIC = b'T\t|\n'

def send_handshake(sock):
    sock.sendall(HANDSHAKE_MAGIC)
    print(f"[+] Sent handshake: {HANDSHAKE_MAGIC.hex()}")

def send_command(sock, command: str):
    cmd_bytes = (command + '\n').encode('utf-8')
    sock.sendall(cmd_bytes)
    print(f"[+] Sent command: {command} ({len(cmd_bytes)} bytes)")

def read_response_with_timeout(sock, timeout=5):
    sock.settimeout(timeout)
    try:
        header = sock.recv(1, socket.MSG_PEEK)
        if not header:
            print("[!] No response received")
            return None
            
        response = b''
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk
                if b'\x05' in response:
                    break
            except socket.timeout:
                break
        return response
    except Exception as e:
        print(f"[!] Error receiving response: {e}")
        return None
    finally:
        sock.settimeout(None)

def parse_response(response_data):
    if not response_data:
        return
    print("[+] Raw response length:", len(response_data))
    print("[+] Response hex dump:", response_data.hex()[:100] + "..." if len(response_data) > 50 else response_data.hex())
    
    try:
        text = response_data.decode('utf-8', errors='replace')
        print("[+] Response as text:\n", text)
    except:
        pass

    try:
        i = 0
        messages = []
        while i < len(response_data):
            if response_data[i] == 0x05:
                print("[+] End marker found")
                break
            elif response_data[i] == 0x03:
                i += 1
                continue
            elif response_data[i] == 0x02:
                if i + 5 <= len(response_data):
                    length = struct.unpack('<I', response_data[i+1:i+5])[0]
                    if i + 5 + length <= len(response_data):
                        message = response_data[i+5:i+5+length]
                        messages.append(message)
                        i += 5 + length
                        continue
            i += 1
        if messages:
            print("[+] Parsed messages:")
            for idx, msg in enumerate(messages, 1):
                try:
                    print(f"  Message {idx}: {msg.decode('utf-8')}")
                except:
                    print(f"  Message {idx}: {msg} (binary)")
    except Exception as e:
        print(f"[!] Error parsing response: {e}")

def main():
    host = 'ctf1.sentinel-cyber.sg'
    port = 65432

    commands = ["employees", "expenses", "top_kpop", "top_hiphop", "favorite_dishes", "flag"]

    for command in commands:
        print(f"\n[+] Trying command: {command}")
        try:
            with socket.create_connection((host, port), timeout=10) as sock:
                print("[+] Connected.")
                
                send_handshake(sock)  # <-- New addition
                
                initial_response = read_response_with_timeout(sock, timeout=2)
                if initial_response:
                    parse_response(initial_response)

                send_command(sock, command)
                time.sleep(0.5)

                response_data = read_response_with_timeout(sock)
                parse_response(response_data)

        except ConnectionResetError as e:
            print(f"[!] Connection reset: {e}")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(1)

if __name__ == '__main__':
    main()
