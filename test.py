
import speedtest

def get_speed(server_choice):
    st = speedtest.Speedtest()
    servers = st.get_servers()
    
    # Define server choices
    server_dict = {
        "BD": "Bangladesh",
        "IND": "India",
        "SG": "Singapore",
        "USA": "United States",
        "UK": "United Kingdom"
    }
    
    if server_choice in server_dict:
        server_list = [server for server_group in servers.values() for server in server_group if server_dict[server_choice] in server['country']]
        if server_list:
            st.get_best_server(server_list)
        else:
            print(f"No servers found for {server_dict[server_choice]}. Using the best available server.")
            st.get_best_server()
    else:
        st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps

    return download_speed, upload_speed

if __name__ == "__main__":
    print("Welcome to the Speed Test Program!")
    print("Would you like to select an auto server or a manual server?")
    print("If auto server, type 'AUTO'. If manual server, type the server name (BD, IND, SG, USA, UK).")
    server_choice = input("Enter your choice: ").upper()
    
    print("Speed test is running...")
    download_speed, upload_speed = get_speed(server_choice)
    print(f"Your download speed is: {download_speed:.2f} Mbps")
    print(f"Your upload speed is: {upload_speed:.2f} Mbps")

