# main_automation.py
import os
import sys
import logging
from datetime import datetime
import git
from obswebsocket import obsws, requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Configure logging
logging.basicConfig(
    filename='livestream_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LivestreamAutomation:
    def __init__(self):
        self.obs_host = "localhost"
        self.obs_port = 4444
        self.obs_password = "your_password"  # Set this in OBS websocket settings
        self.repo_url = "https://github.com/kaderator2/CAUCCAutomation.git"
        self.working_dir = os.path.dirname(os.path.abspath(__file__))

    def show_error(self, message):
        """Display error message to user and log it"""
        import ctypes
        logging.error(message)
        ctypes.windll.user32.MessageBoxW(0, message, "Livestream Setup Error", 0x10)
        sys.exit(1)

    def update_from_github(self):
        """Pull latest changes from GitHub"""
        try:
            repo = git.Repo(self.working_dir)
            repo.remotes.origin.pull()
            logging.info("Successfully updated from GitHub")
        except Exception as e:
            self.show_error(f"Failed to update from GitHub: {str(e)}")

    def update_slideshow(self):
        """Run the slideshow update script"""
        try:
            import AutoSetupSlideshow
            AutoSetupSlideshow.main()
            logging.info("Successfully updated slideshow")
        except Exception as e:
            self.show_error(f"Failed to update slideshow: {str(e)}")

    def setup_obs(self):
        """Initialize OBS and set up initial scene"""
        try:
            ws = obsws(self.obs_host, self.obs_port, self.obs_password)
            ws.connect()
            
            # Set initial scene to Slideshow
            ws.call(requests.SetCurrentScene("Slideshow"))
            
            logging.info("Successfully set up OBS")
            return ws
        except Exception as e:
            self.show_error(f"Failed to setup OBS: {str(e)}")

    def setup_youtube(self):
        """Set up YouTube stream"""
        # YouTube API setup code here
        # Will implement in next message due to length
        pass

    def start_stream(self, obs_ws):
        """Start streaming and recording"""
        try:
            obs_ws.call(requests.StartStreaming())
            obs_ws.call(requests.StartRecording())
            logging.info("Successfully started streaming and recording")
        except Exception as e:
            self.show_error(f"Failed to start streaming: {str(e)}")

    def run(self):
        """Main execution flow"""
        try:
            logging.info("Starting livestream automation")
            
            # Update from GitHub
            self.update_from_github()
            
            # Update slideshow
            self.update_slideshow()
            
            # Setup OBS
            obs_ws = self.setup_obs()
            
            # Setup YouTube
            self.setup_youtube()
            
            # Wait until 9:20 to start stream
            current_time = datetime.now()
            target_time = current_time.replace(hour=9, minute=20, second=0, microsecond=0)
            if current_time < target_time:
                time.sleep((target_time - current_time).total_seconds())
            
            # Start stream
            self.start_stream(obs_ws)
            
            logging.info("Livestream setup completed successfully")
            
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    automation = LivestreamAutomation()
    automation.run()
