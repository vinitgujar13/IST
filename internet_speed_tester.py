import speedtest
import tkinter as tk

def test_speed():
    try:
        # Create a Speedtest object to access the speedtest.net API
        st = speedtest.Speedtest()
        
        # Update UI to show progress and find the best server
        status_label.config(text="Finding best server...")
        root.update()
        st.get_best_server()
        
        # Measure download speed and update status
        status_label.config(text="Testing download speed...")
        root.update()
        download = st.download() / 1_000_000  # Convert it into mb
        
        # Measure upload speed and update status
        status_label.config(text="Testing upload speed...")
        root.update()
        upload = st.upload() / 1_000_000  # Convert it int0 mb
        
        # Get ping
        ping = st.results.ping
        
        # Display results to the user5
        result_label.config(
            text=f"Download Speed: {download:.2f} Mbps\n"
                 f"Upload Speed: {upload:.2f} Mbps\n"
                 f"Ping: {ping:.2f} ms"
        )
        status_label.config(text="Test Completed")

    except Exception as e:
        # to handle any errors that occur during testing
        status_label.config(text="Error occurred")
        result_label.config(text=str(e))

# GUI Setup Code
# Main window setup
root = tk.Tk()  
root.title("Internet Speed Tester")
root.geometry("400x250")

# to show progress
status_label = tk.Label(root, text="Click 'Start Test' to begin", font=("Arial", 12))
status_label.pack(pady=10)
start_button = tk.Button(root, text="Start Test", font=("Arial", 12), command=test_speed)
start_button.pack(pady=15)

# to display test results
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the application event loop
root.mainloop()
