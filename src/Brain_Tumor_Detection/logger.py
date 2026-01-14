import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current timestamp (Month_Day_Year_Hour_Minute_Second).
Log_File = f"log_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path for the 'logs' directory in the current working directory.
logs_path = os.path.join(os.getcwd(), "logs")

# Create the 'logs' directory if it doesn't already exist.
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file within the 'logs' directory.
LOG_FILE_PATH = os.path.join(logs_path, Log_File)

# Configure the logging system.
logging.basicConfig(
    # Set the log recording level to INFO.
    level=logging.INFO,
    
    # Specify the format for log entries: [Timestamp] LineNumber LoggerName - Level - Message
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    # Define handlers to output logs to both a file and the console (terminal).
    handlers=[
        # Writes log entries to the specified file.
        logging.FileHandler(LOG_FILE_PATH),
        
        # Outputs log entries to the standard output (terminal/console).
        logging.StreamHandler()
    ]
)


