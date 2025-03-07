import tkinter as tk
import random
import time
import threading
import math
import os
import requests
import io
import base64
from PIL import Image, ImageDraw, ImageFont, ImageSequence, ImageTk, ImageGrab
from tkinter import font, messagebox, simpledialog, filedialog
from typing import List, Tuple

class RadRainbowASCII:
    """1990s Themed Rainbow ASCII Art GUI Application with PNGUIN and Cyber themes"""
    
    # ASCII Art Collections
    ASCII_PATTERNS = [
        """
        ████████╗██╗  ██╗███████╗    ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
        ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██║████╗  ██║
           ██║   ███████║█████╗      ██████╔╝██╔██╗ ██║██║  ███╗██║   ██║██║██╔██╗ ██║
           ██║   ██╔══██║██╔══╝      ██╔═══╝ ██║╚██╗██║██║   ██║██║   ██║██║██║╚██╗██║
           ██║   ██║  ██║███████╗    ██║     ██║ ╚████║╚██████╔╝╚██████╔╝██║██║ ╚████║
           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                            ▒█▀█▀█▒█▀█▒█▀█▀█▒█▀█▒█▀█▀█
                            ░█▀█▀█░█▀█░█▀█▀█░█▀█░█▀█▀█
                            ░█▀█▀█░█▀█░█▀█▀█░█▀█░█▀█▀█
        """,
        """
        /~~~~~~\\
       /`    -s- ~~~~\\
      /`::::      ~~~~
     /`:::::     :
    /` :::::...::::
   /`   `:::::::::::
        """,
        """
        ╔═══╗╔═══╗╔═══╗╔╗╔╗   ╔════╗╔═╗ ╔╗╔═══╗╔╗ ╔╗╔══╗╔═╗ ╔╗
        ║╔═╗║║╔═╗║║╔══╝║║║║   ║╔╗╔╗║║║╚╗║║║╔═╗║║║ ║║║╔╗║║║╚╗║║
        ║║─║║║║─║║║║╔═╗║╚╝║   ╚╝║║╚╝║╔╗╚╝║║║─║║║║ ║║║║║║║╔╗╚╝║
        ║╚═╝║║╚═╝║║║╚╗║╚═╗║   ──║║──║║╚╗║║║╚═╝║║║ ║║║║║║║║╚╗║║
        ║╔═╗║║╔═╗║║╚═╝║─╔╝║   ──║║──║║ ║║║║╔═╗║║╚═╝║║╚╝║║║ ║║║
        ╚╝─╚╝╚╝─╚╝╚═══╝─╚═╝   ──╚╝──╚╝ ╚═╝╚╝─╚╝╚═══╝╚══╝╚╝ ╚═╝
                      █▄█ █▀█ █▀█ █▄█
                      ░█░ █▄█ █▄█ ░█░
        """,
        """
         █████╗ ███████╗ ██████╗██╗██╗        ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
        ██╔══██╗██╔════╝██╔════╝██║██║        ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██║████╗  ██║
        ███████║███████╗██║     ██║██║        ██████╔╝██╔██╗ ██║██║  ███╗██║   ██║██║██╔██╗ ██║
        ██╔══██║╚════██║██║     ██║██║        ██╔═══╝ ██║╚██╗██║██║   ██║██║   ██║██║██║╚██╗██║
        ██║  ██║███████║╚██████╗██║███████╗   ██║     ██║ ╚████║╚██████╔╝╚██████╔╝██║██║ ╚████║
        ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚══════╝   ╚═╝     ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                   ▄▀▄▀▄▀▄▀▄▀▄▀▄              
                   █▀▄▀▄▀▄▀▄▀▄▀█        
                   █▄▀▄▀▄▀▄▀▄▀▄█                
        """,
        """
        ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗    ██████╗ ██╗      █████╗ ███╗   ██╗███████╗████████╗
        ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
        ███████║███████║██║     █████╔╝        ██║   ███████║█████╗      ██████╔╝██║     ███████║██╔██╗ ██║█████╗     ██║   
        ██╔══██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝      ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔══╝     ██║   
        ██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗    ██║     ███████╗██║  ██║██║ ╚████║███████╗   ██║   
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                                  ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
                                                  ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██║████╗  ██║
                                                  ██████╔╝██╔██╗ ██║██║  ███╗██║   ██║██║██╔██╗ ██║
                                                  ██╔═══╝ ██║╚██╗██║██║   ██║██║   ██║██║██║╚██╗██║
                                                  ██║     ██║ ╚████║╚██████╔╝╚██████╔╝██║██║ ╚████║
                                                  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
        """,
        """
        ▀█▀ █▄█ █▀▀   █▀█ █▀▀ ▀█▀ █░█░█ █▀█ █▀█ █▄▀   █▀█ █▄░█ █▀▀ █░█ █ █▄░█
        ░█░ ░█░ ██▄   █▄█ ██▄ ░█░ ▀▄▀▄▀ █▄█ █▀▄ █░█   █▀▀ █░▀█ █▄█ █▄█ █ █░▀█

                  ▒█▀▀█ ░█▀▀█ ▒█▀▀▄ ▀█▀ ▒█▀▀▀█   ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ 
                  ▒█▄▄▀ ▒█▄▄█ ▒█░▒█ ▒█░ ░▀▀▀▄▄   ▒█░░░ ▒█▄▄█ ░▀▀▀▄▄ 
                  ▒█░▒█ ▒█░▒█ ▒█▄▄▀ ▄█▄ ▒█▄▄▄█   ▒█▄▄█ ▒█░░░ ▒█▄▄▄█
        """,
        """
            ╔═══════════ PNGUIN OS v3.1 ═════════════╗
            _____   
            ( o o )  TERMINAL ACCESS GRANTED
            (  >  )  IP: 127.0.0.1
            /  ^  \\  USER: HACKR_1995
            \\____/   STATUS: CONNECTED
            
            ░█▀█░█▀█░█▀▀░█░█░▀█▀░█▀█░░░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█
            ░█▀▀░█░█░█░█░█░█░░█░░█░█░░░█▀▀░░█░░█▀▀░░█░░█▀▀░█░█
            ░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░░░░▀░░▀░░░▀▀▀░▀▀▀░▀░▀
            ╚═════════════════════════════════════════╝
        """,
        """
            ╔════════════════════════════════════╗
            ║      ██╗    ██╗██╗███╗   ██╗       ║
            ║      ██║    ██║██║████╗  ██║       ║
            ║      ██║ █╗ ██║██║██╔██╗ ██║       ║
            ║      ██║███╗██║██║██║╚██╗██║       ║
            ║      ╚███╔███╔╝██║██║ ╚████║       ║
            ║       ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝       ║
            ║       PNGUIN Edition 9.5           ║
            ║                                    ║
            ║    ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░          ║
            ║                                    ║
            ║    Starting Windows...             ║
            ╚════════════════════════════════════╝
        """,
        """
            ┌─────────── America OnLINUX ───────────┐
            │                                       │
            │      ▄▀▄▀▄ WELCOME! ▄▀▄▀▄             │
            │      █▀█ █▀█ █▀▀ █░█ █ █▄░█           │
            │      █▀▀ █▄█ █▄█ █▄█ █ █░▀█           │
            │                                       │
            │ ┌─────────────────────────────────┐  │
            │ │ Screen Name: PNGUIN_H4CK3R      │  │
            │ └─────────────────────────────────┘  │
            │ ┌─────────────────────────────────┐  │
            │ │ Password: **************        │  │
            │ └─────────────────────────────────┘  │
            │                                       │
            │        [SIGN ON]    [CANCEL]         │
            │                                       │
            │   You've Got Mail! (3 New Messages)   │
            └───────────────────────────────────────┘
        """,
        """
            ▒█▓▒█▓█▀▄▀█▓░▒█▓█▒▓▒
            ▓█▒▓█▒█▓▒▀▀█▒▓▒█▓▒▓█
            █▒▓   _____   ▒█▓▒▓█
            ▓█▒▓  ( o o )  ▒▓▒█▓
            ▒█▓▒  (  >  )  ▓▒▓█▒
            ▓█▒▓  /  ^  \\  ▒█▓▒▓
            █▓▒▓  \\____/   ▓█▒▓█
            ▓█▒▓ THE PNGUIN KNOWS
            ▒█▓▒█▓▒██▒█▓▒▓█▒▓▒█▓
            ▓█▒▓█▒▓█▒▓█▒▓█▒▓█▒▓█
            ☠️ WAKE UP PNGUIN ☠️
        """,
        """
            ┌─[PNGUIN@CYBERDECK]─[~/hack]
            └──╼ $ sudo nmap -sS -p- 10.0.0.1
            
            Starting Nmap 7.95 ( https://pnguin.org ) at 1995-03-07 13:37 UTC
            Interesting ports on target (10.0.0.1):
            PORT    STATE SERVICE
            21/tcp  open  ftp
            22/tcp  open  ssh
            80/tcp  open  http
            443/tcp open  https
                _____
                ( o o )  TARGET ACQUIRED
                (  >  )  DEPLOYING PNGUIN PAYLOAD
                /  ^  \\  STATUS: INJECTING...
                \\____/
            
            ┌─[PNGUIN@CYBERDECK]─[~/hack]
            └──╼ $ _
        """,
        """
            ┌─────────────────────────────────────┐
            │    Windows                       [X] │
            ├─────────────────────────────────────┤
            │                 _____               │
            │                ( o o )              │
            │                (  >  )              │
            │         ░      /  ^  \\      ░       │
            │         ▒      \\____/       ▒       │
            │         ▓                    ▓       │
            │                                      │
            │    PNGUIN.EXE has caused a General   │
            │    Protection Fault in module        │
            │    KERNEL32.DLL at 0137:BFF8D680     │
            │                                      │
            │           [Close] [Ignore]           │
            └─────────────────────────────────────┘
        """,
        """
            ┌─── PNGUIN CHAT ROOM (12 USERS) ─────┐
            │                                     │
            │ HackerDude95: anyone know how to    │
            │               hack email? asking    │
            │               for a friend lol      │
            │                                     │
            │ PNGU1N_SYS: ░█▀█░█▀█░█▀▀░█░█░▀█▀░█▀█│
            │             ░█▀▀░█░█░█░█░█░█░░█░░█░█│
            │             ░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀│
            │                                     │
            │ AOL_MOD: Please keep chat friendly! │
            │                                     │
            │ L33tC0d3r: Check out my new ASCII:  │
            │   _____                             │
            │  ( o o )  <-- Super Elite Penguin   │
            │  (  >  )                            │
            │  /  ^  \\                            │
            │  \\____/                             │
            │                                     │
            └─────────────────────────────────────┘
        """,
        """
            ┌──── PNGUIN NET DIALER v1.2 ─────┐
            │                                 │
            │  ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌  │
            │  ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌░░░░░░░░░░░░░░  │
            │                                 │
            │  Dialing... 555-PNGUIN-95       │
            │                                 │
            │  CONNECT 28.8KBPS               │
            │                                 │
            │  ▒▒▓█▓▒▓█▒▓█▒▓█▒▓█HANDSHAKE▓█▒▓  │
            │  ▓█▒▓█▒▓█▒▓█NEGOTIATING▒▓█▒▓█▒▓  │
            │  ▒▓█▒▓█▒LOGIN SUCCESSFUL▓█▒▓█▒▓  │
            │                                 │
            │      _____   CONNECTION         │
            │     ( o o )  ESTABLISHED        │
            │     (  >  )  DOWNLOADING...     │
            │     /  ^  \\  20.3KB/S           │
            │     \\____/                      │
            │                                 │
            └─────────────────────────────────┘
        """,
        """
            ╔═════ PNGUIN BULLETIN BOARD SYSTEM ═════╗
            ║                                        ║
            ║  ▀█▀ █░█ █▀▀   █▀█ █▄░█ █▀▀ █░█ █ █▄░█ ║
            ║  ░█░ █▀█ █▀▀   █▀▀ █░▀█ █▄█ █▄█ █ █░▀█ ║
            ║  ▀▀▀ ▀░▀ ▀▀▀   ▀░░ ▀░░▀ ▀░▀ ▀░▀ ▀ ▀░░▀ ║
            ║                                        ║
            ║  [1] Download ASCII Art Files          ║
            ║  [2] Message Boards                    ║
            ║  [3] Multi-User Chat                   ║
            ║  [4] Internet Gateway                  ║
            ║  [5] File Sharing Networks             ║
            ║  [X] Exit BBS                          ║
            ║                                        ║
            ║  SYSOP: PNGUIN_LORD                    ║
            ║  USERS ONLINE: 13                      ║
            ║  YOUR TIME REMAINING: 59 MINUTES       ║
            ║                                        ║
            ║     _____                              ║
            ║    ( o o )  "Join the Revolution!"     ║
            ║    (  >  )                             ║
            ║    /  ^  \\                             ║
            ║    \\____/                              ║
            ╚════════════════════════════════════════╝
        """,
        """
            ┌──────────── PNGUIN SECURITY SYSTEM ────────────┐
            │ ACCESS LEVEL: ROOT                 [ENCRYPTED] │
            ├──────────────────────────────────────────────┤
            │                                              │
            │    _____     _____     _____     _____       │
            │   ( o o )   ( o o )   ( o o )   ( o o )      │
            │   (  >  )   (  >  )   (  >  )   (  >  )      │
            │   /  ^  \\   /  ^  \\   /  ^  \\   /  ^  \\      │
            │   \\____/    \\____/    \\____/    \\____/       │
            │                                              │
            │   FIREWALL   NET_MON    SNIFFER    IDS       │
            │   ENABLED    ACTIVE     RUNNING    ALERT!    │
            │                                              │
            │ $ ./pnguin-trace.sh 192.168.1.1              │
            │ > TARGET FOUND - INITIATING COUNTERMEASURES  │
            │ > ▓▒░DEPLOYING PENGUIN ARMY░▒▓               │
            │ > ░░▒▓█▓▒▓█▒▓█▒▓HACKING MAINFRAME▓█▒▓█▒▓█▒▓  │
            │                                              │
            │ $ sudo rm -rf /intruder/*                    │
            │ > ACCESS REVOKED. INTRUDER EJECTED.          │
            │                                              │
            └──────────────────────────────────────────────┘
        """
    ]
    
    SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\~`"
    
    # Non-green vibrant colors on black
    COLORS = [
        "#FF5733",  # Bright Red
        "#FFC300",  # Yellow
        "#FF33A8",  # Hot Pink
        "#33A8FF",  # Bright Blue
        "#A833FF",  # Purple
        "#FF5733",  # Orange
        "#FF33FF",  # Magenta
        "#33FFFF",  # Cyan
        "#8B4513",  # Saddle Brown (for retro)
    ]

    # Black theme colors
    BLACK_COLORS = [
        "#000000",  # Black
        "#111111",  # Dark Gray
        "#222222",  # Gray
        "#333333",  # Light Gray
        "#444444",  # Almost White
    ]
    
    def __init__(self, root: tk.Tk):
        """Initialize the application"""
        self.root = root
        root.title("PNGUIN CYBERDECK v1.2")
        
        # Initially hide the main window until splash is done
        root.withdraw()
        
        # Configure the window
        self.width, self.height = 900, 600
        root.geometry(f"{self.width}x{self.height}")
        root.configure(bg="#000000")
        
        # Animation state
        self.is_animating = False
        self.animation_speed = 100  # milliseconds
        self.frame_count = 0
        self.matrix_chars = []
        self.last_time = time.time()
        self.fps_count = 0
        self.fps = 0
        
        # Set default animation to prevent errors
        self.current_animation = None
        
        # Animation clip management
        self.animation_scenes = []
        self.current_scene_name = ""
        self.scene_editor_open = False
        
        # Ollama chat management
        self.ollama_chat_open = False
        self.ollama_chat_messages = []
        self.ollama_model_var = None
        self.ollama_available_models = []
        
        # A system prompt for the Ollama chat
        self.ollama_system_prompt = "You are an ASCII companion inside a retro-themed application."

        self.setup_fonts()
        
        # Show boot splash screen
        self.show_boot_splash()
        
        # Initialize sound (simulated)
        self.modem_connected = False
    
    def setup_fonts(self):
        """Set up the fonts for the application"""
        self.title_font = font.Font(family="Courier", size=14, weight="bold")
        self.ascii_font = font.Font(family="Courier", size=12)
        self.menu_font = font.Font(family="Courier", size=10)
        self.status_font = font.Font(family="Terminal", size=9)
        self.button_font = font.Font(family="Courier", size=9, weight="bold")
    
    def show_boot_splash(self):
        """Show a clean black boot splash loading screen"""
        # Create a splash screen
        splash = tk.Toplevel(self.root)
        splash.title("")
        splash.geometry("500x300")
        splash.configure(bg="#000000")
        splash.overrideredirect(True)  # No window decorations
        
        # Ensure the splash screen appears on top
        splash.attributes("-topmost", True)
        
        # Center the splash screen
        splash.update_idletasks()
        width = splash.winfo_width()
        height = splash.winfo_height()
        x = (splash.winfo_screenwidth() // 2) - (width // 2)
        y = (splash.winfo_screenheight() // 2) - (height // 2)
        splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        # Make sure it's visible
        splash.lift()
        splash.focus_force()
        
        # PNGUIN ASCII Logo
        pnguin_logo = """
        ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
        ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██║████╗  ██║
        ██████╔╝██╔██╗ ██║██║  ███╗██║   ██║██║██╔██╗ ██║
        ██╔═══╝ ██║╚██╗██║██║   ██║██║   ██║██║██║╚██╗██║
        ██║     ██║ ╚████║╚██████╔╝╚██████╔╝██║██║ ╚████║
        ╚═╝     ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
        """
        
        logo_label = tk.Label(
            splash,
            text=pnguin_logo,
            font=("Courier", 10, "bold"),
            bg="#000000",
            fg="#33FFFF",
            justify=tk.CENTER
        )
        logo_label.pack(pady=(30, 10))
        
        # Version text
        version_label = tk.Label(
            splash,
            text="CYBERDECK v1.2",
            font=("Courier", 14, "bold"),
            bg="#000000",
            fg="#FF33FF",
            justify=tk.CENTER
        )
        version_label.pack(pady=10)
        
        # Loading bar frame
        loading_frame = tk.Frame(splash, bg="#000000", height=20, width=300)
        loading_frame.pack(pady=20)
        
        # Create loading bar
        loading_canvas = tk.Canvas(
            loading_frame,
            width=300,
            height=20,
            bg="#000000",
            highlightthickness=1,
            highlightbackground="#333333"
        )
        loading_canvas.pack()
        
        # Simulate loading progress
        self.simulate_loading(splash, loading_canvas, 0)
    
    def simulate_loading(self, splash, canvas, progress):
        """Simulate a loading progress sequence"""
        # Update progress
        progress += random.randint(1, 5)
        if progress > 100:
            progress = 100
        
        # Draw progress bar
        canvas.delete("progress")
        canvas.create_rectangle(
            2, 2, 2 + (progress * 296 / 100), 18,
            fill=random.choice(self.COLORS),
            outline="",
            tags="progress"
        )
        
        # Keep splash on top
        splash.lift()
        
        # Continue or finish
        if progress < 100:
            self.root.after(random.randint(50, 150), lambda: self.simulate_loading(
                splash, canvas, progress
            ))
        else:
            # Loading complete, close splash after a small delay
            self.root.after(500, lambda: self.finish_loading(splash))
    
    def finish_loading(self, splash):
        """Finish the loading process and setup the main UI"""
        splash.destroy()
        self.setup_ui()
        
        # Show the main window now that splash is gone
        self.root.deiconify()
        self.root.update()
        
        # Make sure main window is on top
        self.root.lift()
        self.root.focus_force()
        
        self.simulate_modem_connection()
    
    def setup_ui(self):
        """Set up the user interface with a sidebar layout"""
        # Main container frame
        main_container = tk.Frame(self.root, bg="#000000")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left sidebar (1/5 of width)
        self.sidebar = tk.Frame(main_container, bg="#111111", width=180)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=2, pady=2)
        # Force the width
        self.sidebar.pack_propagate(False)
        
        # Title in sidebar
        sidebar_title = tk.Label(
            self.sidebar,
            text="PNGUIN\nCYBERDECK\nv1.2",
            bg="#111111",
            fg="#FF33FF",
            font=self.title_font,
            justify=tk.CENTER
        )
        sidebar_title.pack(pady=20)
        
        # Separator
        separator = tk.Frame(self.sidebar, height=2, bg="#333333")
        separator.pack(fill=tk.X, padx=10, pady=10)
        
        # Control buttons in sidebar
        button_configs = [
            ("Start Animation", self.toggle_animation),
            ("Stop Animation", self.stop_animation),
            ("Random Pattern", self.new_pattern),
            ("Matrix Mode", self.matrix_mode),
            ("Rainbow Mode", self.rainbow_mode),
            ("Cyber Wave", self.cyber_wave_mode),
            ("Connect", self.connect),
            ("Scene Editor", self.open_scene_editor),
            ("Generate GIF", self.generate_gif_from_scenes),
            ("Open ASCII", self.open_file),
            ("Ollama API", self.call_ollama_api),
            ("Ollama Chat", self.open_ollama_chat),
            ("Help", self.help_text),
            ("Exit", self.exit_app)
        ]
        
        for text, cmd in button_configs:
            btn = tk.Button(
                self.sidebar,
                text=text,
                bg="#000000",  # Black buttons
                fg="#33FFFF",
                relief=tk.RAISED,
                borderwidth=1,
                command=cmd,
                font=self.button_font,
                width=16,
                height=1,
                activebackground="#222222",
                activeforeground="#FF33FF"
            )
            btn.pack(pady=5, padx=10)
            
            # Add hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#222222"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#000000"))
        
        # Speed control
        speed_frame = tk.Frame(self.sidebar, bg="#111111")
        speed_frame.pack(pady=10)
        
        tk.Label(
            speed_frame, 
            text="Speed Control",
            bg="#111111", 
            fg="#FFC300", 
            font=self.status_font
        ).pack()
        
        self.speed_scale = tk.Scale(
            speed_frame,
            from_=10,
            to=200,
            orient=tk.HORIZONTAL,
            length=150,
            bg="#111111",
            fg="#FFC300",
            troughcolor="#000000",
            highlightthickness=0,
            command=self.change_speed
        )
        self.speed_scale.set(self.animation_speed)
        self.speed_scale.pack(pady=5)
        
        # Create right container to hold both content and scene editor
        right_container = tk.Frame(main_container, bg="#000000")
        right_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Main content area
        content_container = tk.Frame(right_container, bg="#000000")
        content_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scene editor sidebar (initially hidden)
        self.scene_editor_sidebar = tk.Frame(right_container, bg="#111111", width=200)
        self.scene_editor_sidebar.pack_propagate(False)
        # Hidden by default
        
        # Scene editor content
        tk.Label(
            self.scene_editor_sidebar,
            text="SCENE EDITOR",
            bg="#111111",
            fg="#FF33FF",
            font=self.title_font
        ).pack(pady=10)
        
        # Add scene button
        tk.Button(
            self.scene_editor_sidebar,
            text="+ Capture Scene",
            bg="#000000",
            fg="#33FFFF",
            command=self.capture_current_scene,
            font=self.button_font
        ).pack(fill=tk.X, padx=10, pady=5)
        
        # Scene list frame with scrollbar
        scene_list_frame = tk.Frame(self.scene_editor_sidebar, bg="#111111")
        scene_list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scene_scrollbar = tk.Scrollbar(scene_list_frame)
        scene_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scene_listbox = tk.Listbox(
            scene_list_frame,
            bg="#000000",
            fg="#33FFFF",
            selectbackground="#333333",
            selectforeground="#FF33FF",
            font=self.status_font,
            height=15,
            yscrollcommand=scene_scrollbar.set
        )
        self.scene_listbox.pack(fill=tk.BOTH, expand=True)
        scene_scrollbar.config(command=self.scene_listbox.yview)
        
        # Scene controls
        scene_controls_frame = tk.Frame(self.scene_editor_sidebar, bg="#111111")
        scene_controls_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(
            scene_controls_frame,
            text="↑",
            bg="#000000",
            fg="#33FFFF",
            command=self.move_scene_up,
            width=3
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            scene_controls_frame,
            text="↓",
            bg="#000000",
            fg="#33FFFF",
            command=self.move_scene_down,
            width=3
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            scene_controls_frame,
            text="Delete",
            bg="#000000",
            fg="#FF33A8",
            command=self.delete_scene,
            width=10
        ).pack(side=tk.RIGHT, padx=2)
        
        # Scene duration control
        duration_frame = tk.Frame(self.scene_editor_sidebar, bg="#111111")
        duration_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            duration_frame,
            text="Frame Duration (ms):",
            bg="#111111",
            fg="#33FFFF",
            font=self.status_font
        ).pack(anchor="w")
        
        self.duration_var = tk.StringVar(value="100")
        duration_entry = tk.Entry(
            duration_frame,
            textvariable=self.duration_var,
            bg="#000000",
            fg="#33FFFF",
            insertbackground="#33FFFF",
            width=5,
            font=self.status_font
        )
        duration_entry.pack(anchor="w", pady=5)
        
        # Ollama chat sidebar (initially hidden)
        self.ollama_chat_sidebar = tk.Frame(right_container, bg="#111111", width=300)
        self.ollama_chat_sidebar.pack_propagate(False)
        
        # Chat header
        self.ollama_chat_header = tk.Label(
            self.ollama_chat_sidebar,
            text="OLLAMA CHAT",
            bg="#111111",
            fg="#FF33FF",
            font=self.title_font
        )
        self.ollama_chat_header.pack(pady=10)
        
        # Model selection
        model_frame = tk.Frame(self.ollama_chat_sidebar, bg="#111111")
        model_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            model_frame,
            text="Model:",
            bg="#111111",
            fg="#33FFFF",
            font=self.menu_font,
            anchor="w"
        ).pack(side=tk.LEFT)
        
        self.ollama_model_var = tk.StringVar()
        self.ollama_model_dropdown = tk.OptionMenu(model_frame, self.ollama_model_var, ())
        self.ollama_model_dropdown.config(bg="#000000", fg="#33FFFF", width=20, highlightbackground="#333333")
        self.ollama_model_dropdown.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Chat display
        chat_display_frame = tk.Frame(self.ollama_chat_sidebar, bg="#111111")
        chat_display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.ollama_chat_text = tk.Text(
            chat_display_frame,
            bg="#000000",
            fg="#33FFFF",
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=self.status_font
        )
        self.ollama_chat_text.pack(fill=tk.BOTH, expand=True)
        
        # Chat input
        chat_input_frame = tk.Frame(self.ollama_chat_sidebar, bg="#111111")
        chat_input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.ollama_chat_entry = tk.Entry(chat_input_frame, bg="#000000", fg="#33FFFF", font=self.status_font, insertbackground="#33FFFF")
        self.ollama_chat_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        send_btn = tk.Button(chat_input_frame, text="Send", bg="#000000", fg="#33FFFF", command=self.ollama_send_message)
        send_btn.pack(side=tk.LEFT)
        
        # Main content area
        self.content_frame = tk.Frame(
            content_container, 
            relief=tk.SUNKEN, 
            borderwidth=2, 
            bg="#000000"
        )
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # ASCII art canvas
        self.canvas = tk.Canvas(
            self.content_frame,
            bg="#000000",
            bd=0,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = tk.Frame(content_container, bg="#111111", relief=tk.SUNKEN, borderwidth=1)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(5, 0))
        
        self.status_text = tk.Label(
            self.status_bar, 
            text="Initializing system...",
            bg="#111111",
            fg="#33FFFF",
            font=self.status_font,
            anchor=tk.W
        )
        self.status_text.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.fps_label = tk.Label(
            self.status_bar,
            text="FPS: 0",
            bg="#111111",
            fg="#33FFFF",
            font=self.status_font
        )
        self.fps_label.pack(side=tk.RIGHT, padx=5)
        
        # Connection indicator
        self.connection_indicator = tk.Label(
            self.status_bar,
            text="⚫ OFFLINE",
            bg="#111111",
            fg="#FF33A8",
            font=self.status_font
        )
        self.connection_indicator.pack(side=tk.RIGHT, padx=10)
        
        # Scenes indicator
        self.scenes_indicator = tk.Label(
            self.status_bar,
            text="Scenes: 0",
            bg="#111111",
            fg="#33FFFF",
            font=self.status_font
        )
        self.scenes_indicator.pack(side=tk.RIGHT, padx=10)
        
        # Bind resize event
        self.root.bind("<Configure>", self.on_resize)
    
    def on_resize(self, event):
        """Handle window resize events"""
        if event.widget == self.root and (abs(self.width - event.width) > 10 or abs(self.height - event.height) > 10):
            self.width, self.height = event.width, event.height
            
            # Update any size-dependent elements
            if self.is_animating:
                self.canvas.delete("all")  # Clear the canvas
                self.matrix_chars = []  # Reset matrix characters
    
    def simulate_modem_connection(self):
        """Simulate connecting a modem"""
        self.status_text.config(text="Establishing connection...")
        
        # Start a thread to simulate the connection process
        threading.Thread(target=self._modem_connection_thread, daemon=True).start()
    
    def _modem_connection_thread(self):
        """Simulated modem connection in a separate thread"""
        time.sleep(1.5)  # Simulating connection
        self.root.after(0, lambda: self.status_text.config(text="Initializing protocols..."))
        
        time.sleep(1)  # Simulating handshake
        self.root.after(0, lambda: self.status_text.config(text="Connection established. Ready."))
        self.root.after(0, lambda: self.connection_indicator.config(text="⚫ ONLINE", fg="#33FF33"))
        
        self.modem_connected = True
        
        # Display a static ASCII art
        self.root.after(500, self.new_pattern)
    
    def new_pattern(self):
        """Generate a new random ASCII pattern"""
        if self.is_animating:
            self.toggle_animation()  # Stop animation first
        
        self.canvas.delete("all")  # Clear the canvas
        
        # Display a static ASCII art
        current_ascii = random.choice(self.ASCII_PATTERNS)
        self.canvas.create_text(
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() // 2,
            text=current_ascii,
            font=self.ascii_font,
            fill=random.choice(self.COLORS),
            tags="ascii"
        )
        
        self.status_text.config(text="Generated new ASCII pattern.")
    
    def toggle_animation(self):
        """Toggle animation on/off"""
        if not self.is_animating:
            self.is_animating = True
            self.status_text.config(text="Animation mode activated.")
            self.frame_count = 0
            self.last_time = time.time()
            self.fps_count = 0
            # Set the default animation first before starting the animation loop
            self.current_animation = self.rainbow_animation
            self.animate()  # Start animation
        else:
            self.stop_animation()
    
    def stop_animation(self):
        """Stop the current animation"""
        if self.is_animating:
            self.is_animating = False
            self.status_text.config(text="Animation stopped.")
            # Clear the canvas
            self.canvas.delete("all")
            # Display a static ASCII art
            self.new_pattern()
    
    def matrix_mode(self):
        """Switch to matrix animation mode"""
        if not self.is_animating:
            self.toggle_animation()
        
        self.current_animation = self.matrix_animation
        self.status_text.config(text="Matrix mode activated.")
    
    def rainbow_mode(self):
        """Switch to rainbow animation mode"""
        if not self.is_animating:
            self.toggle_animation()
        
        self.current_animation = self.rainbow_animation
        self.status_text.config(text="Rainbow mode activated.")
    
    def cyber_wave_mode(self):
        """Switch to cyber wave animation mode"""
        if not self.is_animating:
            self.toggle_animation()
        
        self.current_animation = self.cyber_wave_animation
        self.status_text.config(text="Cyber wave mode activated.")
    
    def animate(self):
        """Perform the animation"""
        if not self.is_animating:
            return
        
        # Clear canvas
        self.canvas.delete("all")
        
        # Update FPS counter
        current_time = time.time()
        elapsed = current_time - self.last_time
        self.fps_count += 1
        
        if elapsed >= 1.0:  # Update FPS every second
            self.fps = self.fps_count / elapsed
            self.fps_label.config(text=f"FPS: {self.fps:.1f}")
            self.fps_count = 0
            self.last_time = current_time
        
        # Call the current animation function if it exists
        if self.current_animation:
            self.current_animation()
        else:
            # Default to rainbow animation if not set
            self.current_animation = self.rainbow_animation
            self.current_animation()
        
        # Increment frame counter
        self.frame_count += 1
        
        # Schedule next animation frame
        self.root.after(self.animation_speed // 10, self.animate)
    
    def rainbow_animation(self):
        """Create a colorful rainbow animation with ASCII art"""
        # Select a random ASCII pattern
        pattern = random.choice(self.ASCII_PATTERNS)
        
        # Create rainbow effect with multiple colored copies
        for i in range(5):
            offset = math.sin(self.frame_count * 0.05 + i * 0.5) * 30
            
            self.canvas.create_text(
                self.canvas.winfo_width() // 2 + offset,
                self.canvas.winfo_height() // 2 + offset / 2,
                text=pattern,
                font=self.ascii_font,
                fill=random.choice(self.COLORS),
                tags="ascii"
            )
            
        # Add a floating message
        if self.frame_count % 100 < 50:  # Blink effect
            hover_y = self.canvas.winfo_height() * 0.85 + math.sin(self.frame_count * 0.1) * 10
            self.canvas.create_text(
                self.canvas.winfo_width() // 2,
                hover_y,
                text="PNGUIN CYBERDECK v1.2",
                font=("Courier", 16, "bold"),
                fill="#FF33FF",
                tags="ascii_message"
            )
    
    def matrix_animation(self):
        """Create a Matrix-style animation (without using green)"""
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Initialize matrix characters if needed
        if not self.matrix_chars:
            num_columns = canvas_width // 15
            self.matrix_chars = []
            
            for i in range(num_columns):
                x = i * 15
                speed = random.uniform(2, 8)
                color = random.choice(self.COLORS)
                self.matrix_chars.append((x, -20, speed, color))
        
        # Update and draw matrix characters
        updated_chars = []
        
        for x, y, speed, color in self.matrix_chars:
            # Draw the character
            char = random.choice(self.SYMBOLS)
            self.canvas.create_text(
                x, y,
                text=char,
                font=("Courier", 14, "bold"),
                fill=color,
                tags="matrix"
            )
            
            # Update position
            y += speed
            
            # Reset if off-screen
            if y > canvas_height:
                y = -20
                x = random.randint(0, canvas_width)
                speed = random.uniform(2, 8)
                color = random.choice(self.COLORS)
            
            updated_chars.append((x, y, speed, color))
        
        self.matrix_chars = updated_chars
        
        # Add new characters occasionally
        if random.random() < 0.1:
            x = random.randint(0, canvas_width)
            speed = random.uniform(2, 8)
            color = random.choice(self.COLORS)
            self.matrix_chars.append((x, -20, speed, color))
    
    def cyber_wave_animation(self):
        """Create a wave of cyber symbols"""
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        wave_chars = "~!@#$%^&*()_+-=[]{}|;:,./<>?"
        pnguin_text = "PNGUIN CYBERDECK"
        
        for i in range(0, canvas_width, 20):
            for j in range(0, canvas_height, 20):
                # Calculate wave effect
                x_offset = math.sin((j / 50) + (self.frame_count * 0.1)) * 10
                y_offset = math.cos((i / 50) + (self.frame_count * 0.1)) * 10
                
                # Decide whether to show a symbol or a letter from pnguin_text
                if random.random() < 0.2:  # 20% chance to show a letter from our text
                    char_index = (i + j + self.frame_count) % len(pnguin_text)
                    char = pnguin_text[char_index]
                else:
                    # Select a symbol
                    char_index = (i + j + self.frame_count) % len(wave_chars)
                    char = wave_chars[char_index]
                
                # Calculate color index using a wave pattern
                color_index = int((math.sin(self.frame_count * 0.05 + i * 0.01 + j * 0.01) + 1) * 4) % len(self.COLORS)
                
                # Draw the character
                self.canvas.create_text(
                    i + x_offset, j + y_offset,
                    text=char,
                    font=("Courier", 14, "bold"),
                    fill=self.COLORS[color_index],
                    tags="cyber"
                )
    
    def change_speed(self, val):
        """Change the animation speed"""
        self.animation_speed = int(val)
    
    def open_file(self):
        """Simulate opening a file with a dialog"""
        filename = simpledialog.askstring(
            "Open File",
            "Enter ASCII file name:",
            initialvalue="PNGUIN.ASC"
        )
        
        if filename:
            self.status_text.config(text=f"Opening {filename}...")
            
            # Simulate file loading
            self.root.after(500, lambda: self.status_text.config(text=f"Loaded {filename}!"))
            
            # Display a random ASCII art
            self.canvas.delete("all")
            current_ascii = random.choice(self.ASCII_PATTERNS)
            self.canvas.create_text(
                self.canvas.winfo_width() // 2,
                self.canvas.winfo_height() // 2,
                text=current_ascii,
                font=self.ascii_font,
                fill=random.choice(self.COLORS),
                tags="ascii"
            )
    
    def open_scene_editor(self):
        """Open the scene editor sidebar"""
        if not self.scene_editor_open:
            # Show the scene editor sidebar
            self.scene_editor_sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
            self.scene_editor_open = True
            self.status_text.config(text="Scene editor opened. Capture scenes to create animated GIF.")
        else:
            # Hide the scene editor sidebar
            self.scene_editor_sidebar.pack_forget()
            self.scene_editor_open = False
            self.status_text.config(text="Scene editor closed.")
    
    def capture_current_scene(self):
        """Capture the current state of the canvas as a scene"""
        if not hasattr(self, 'current_animation') and not any(self.canvas.find_all()):
            messagebox.showinfo("Content Required", "Please start an animation or generate a pattern first!")
            return
        
        # Ask for scene name
        scene_name = simpledialog.askstring(
            "Scene Name",
            "Enter a name for this scene:",
            initialvalue=f"Scene {len(self.animation_scenes) + 1}"
        )
        
        if not scene_name:
            return  # User canceled
        
        # Create a folder for temp frames if it doesn't exist
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_frames")
        os.makedirs(temp_dir, exist_ok=True)
        
        # Generate a unique filename for this scene
        scene_file = os.path.join(temp_dir, f"scene_{len(self.animation_scenes):03d}.png")
        
        # Temporarily pause the animation if it's running
        was_animating = self.is_animating
        if was_animating:
            self.is_animating = False
        
        try:
            # Use screenshot approach to capture the canvas
            self.status_text.config(text="Capturing canvas...")
            self.root.update()
            
            # Get the canvas dimensions and position
            canvas_x = self.canvas.winfo_rootx()
            canvas_y = self.canvas.winfo_rooty()
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # Capture the canvas area using PIL
            screenshot = ImageGrab.grab(bbox=(canvas_x, canvas_y, 
                                             canvas_x + canvas_width, 
                                             canvas_y + canvas_height))
            
            # Save the screenshot
            screenshot.save(scene_file)
            
            # Add to our scenes list
            self.animation_scenes.append({
                "name": scene_name,
                "file": scene_file,
                "animation_type": getattr(self, 'current_animation', None).__name__ if hasattr(self, 'current_animation') else None,
                "frame_count": self.frame_count
            })
            
            # Update the listbox
            self.scene_listbox.insert(tk.END, scene_name)
            self.scenes_indicator.config(text=f"Scenes: {len(self.animation_scenes)}")
            
            self.status_text.config(text=f"Scene '{scene_name}' captured")
            
        except Exception as e:
            # Fallback method if screenshot fails
            try:
                # Create a new image with black background
                img = Image.new('RGB', (self.canvas.winfo_width(), self.canvas.winfo_height()), color='black')
                
                # If this is text-based content, try to render it directly to an image
                items = self.canvas.find_all()
                
                if items:
                    # Get all canvas items
                    for item in items:
                        item_type = self.canvas.type(item)
                        if item_type == "text":
                            # Get text properties
                            text = self.canvas.itemcget(item, "text")
                            x, y = self.canvas.coords(item)
                            fill = self.canvas.itemcget(item, "fill")
                            
                            # Create drawing context
                            draw = ImageDraw.Draw(img)
                            font_size = 12  # Default font size
                            text_font = ImageFont.truetype("Courier", font_size)
                            
                            # Draw text
                            draw.text((x, y), text, fill=fill, font=text_font, anchor="center")
                
                # Save the image
                img.save(scene_file)
                
                # Add to our scenes list
                self.animation_scenes.append({
                    "name": scene_name,
                    "file": scene_file,
                    "animation_type": getattr(self, 'current_animation', None).__name__ if hasattr(self, 'current_animation') else None,
                    "frame_count": self.frame_count
                })
                
                # Update the listbox
                self.scene_listbox.insert(tk.END, scene_name)
                self.scenes_indicator.config(text=f"Scenes: {len(self.animation_scenes)}")
                
                self.status_text.config(text=f"Scene '{scene_name}' captured (fallback method)")
                
            except Exception as inner_e:
                self.status_text.config(text=f"Error capturing scene: {str(e)} - {str(inner_e)}")
                messagebox.showerror("Error", f"Error capturing scene: {str(e)}\nSecondary error: {str(inner_e)}")
        
        finally:
            # Restore animation state
            self.is_animating = was_animating
            if was_animating:
                self.animate()
    
    def move_scene_up(self):
        """Move the selected scene up in the list"""
        selected = self.scene_listbox.curselection()
        if not selected:
            return
        
        index = selected[0]
        if index == 0:
            return  # Already at the top
        
        # Swap scenes in the data
        self.animation_scenes[index], self.animation_scenes[index-1] = self.animation_scenes[index-1], self.animation_scenes[index]
        
        # Update the listbox
        scene_name = self.scene_listbox.get(index)
        self.scene_listbox.delete(index)
        self.scene_listbox.insert(index-1, scene_name)
        self.scene_listbox.selection_set(index-1)
        
        self.status_text.config(text=f"Moved '{scene_name}' up")
    
    def move_scene_down(self):
        """Move the selected scene down in the list"""
        selected = self.scene_listbox.curselection()
        if not selected:
            return
        
        index = selected[0]
        if index == len(self.animation_scenes) - 1:
            return  # Already at the bottom
        
        # Swap scenes in the data
        self.animation_scenes[index], self.animation_scenes[index+1] = self.animation_scenes[index+1], self.animation_scenes[index]
        
        # Update the listbox
        scene_name = self.scene_listbox.get(index)
        self.scene_listbox.delete(index)
        self.scene_listbox.insert(index+1, scene_name)
        self.scene_listbox.selection_set(index+1)
        
        self.status_text.config(text=f"Moved '{scene_name}' down")
    
    def delete_scene(self):
        """Delete the selected scene"""
        selected = self.scene_listbox.curselection()
        if not selected:
            return
        
        index = selected[0]
        scene_name = self.scene_listbox.get(index)
        
        # Ask for confirmation
        if not messagebox.askyesno("Confirm Delete", f"Delete scene '{scene_name}'?"):
            return
        
        # Delete the scene file if it exists
        scene_file = self.animation_scenes[index]["file"]
        if os.path.exists(scene_file):
            try:
                os.remove(scene_file)
            except:
                pass  # Ignore errors on deletion
        
        # Remove from our data
        del self.animation_scenes[index]
        
        # Update the listbox
        self.scene_listbox.delete(index)
        self.scenes_indicator.config(text=f"Scenes: {len(self.animation_scenes)}")
        
        self.status_text.config(text=f"Deleted scene '{scene_name}'")
    
    def generate_gif_from_scenes(self):
        """Generate an animated GIF from the captured scenes"""
        if not self.animation_scenes:
            messagebox.showinfo("No Scenes", "Please capture scenes first using the Scene Editor!")
            if not self.scene_editor_open:
                self.open_scene_editor()
            return
        
        # Ask for filename and location
        filetypes = [("GIF files", "*.gif"), ("All files", "*.*")]
        filename = filedialog.asksaveasfilename(
            title="Save Animated GIF",
            defaultextension=".gif",
            filetypes=filetypes,
            initialfile="PNGUIN_ANIMATION.gif"
        )
        
        if not filename:
            return  # User canceled
        
        self.status_text.config(text="Creating animated GIF from scenes, please wait...")
        self.root.update()
        
        try:
            # Get frame duration from input (with validation)
            try:
                duration = int(self.duration_var.get())
                if duration < 10:
                    duration = 10  # Minimum 10ms
                elif duration > 1000:
                    duration = 1000  # Maximum 1 second
            except ValueError:
                duration = 100  # Default if invalid
            
            # Prepare frames
            frames = []
            for scene in self.animation_scenes:
                if os.path.exists(scene["file"]):
                    frames.append(Image.open(scene["file"]))
            
            if not frames:
                raise Exception("No valid frames found in scenes")
            
            # Save the animated GIF
            frames[0].save(
                filename,
                save_all=True,
                append_images=frames[1:],
                optimize=False,
                duration=duration,  # Duration between frames in milliseconds
                loop=0  # 0 means loop indefinitely
            )
            
            self.status_text.config(text=f"Animated GIF saved as {os.path.basename(filename)}")
            
            messagebox.showinfo(
                "Save Complete",
                f"Your animated GIF has been saved as {os.path.basename(filename)}!"
            )
            
        except Exception as e:
            self.status_text.config(text=f"Error saving GIF: {str(e)}")
            messagebox.showerror("Error", f"Error creating animated GIF: {str(e)}")
    
    def save_animated_gif(self):
        """Legacy method - redirects to the scene editor"""
        if not self.scene_editor_open:
            self.open_scene_editor()
        
        messagebox.showinfo(
            "Scene-Based Animation",
            "Use the Scene Editor to capture scenes and then click 'Generate GIF' to create your animation."
        )
    
    def connect(self):
        """Simulate connecting to a network"""
        if not self.modem_connected:
            self.simulate_modem_connection()
        else:
            # Show a connection dialog
            connect_win = tk.Toplevel(self.root)
            connect_win.title("Connect")
            connect_win.geometry("300x200")
            connect_win.configure(bg="#000000")
            connect_win.transient(self.root)
            
            tk.Label(
                connect_win,
                text="CONNECT TO NETWORK",
                font=self.title_font,
                bg="#000000",
                fg="#FF33FF"
            ).pack(pady=10)
            
            network_options = [
                "☆ PNGUIN NETWORK - Main Hub",
                "☆ ASCII GALLERY - Art Exchange",
                "☆ CYBER CENTRAL - Data Archive",
                "☆ DIGITAL NEXUS - Information Core"
            ]
            
            network_var = tk.StringVar(connect_win)
            network_var.set(network_options[0])
            
            option_menu = tk.OptionMenu(connect_win, network_var, *network_options)
            option_menu.config(bg="#000000", fg="#33FFFF", width=25, highlightbackground="#333333")
            option_menu.pack(pady=10)
            
            button_frame = tk.Frame(connect_win, bg="#000000")
            button_frame.pack(pady=10)
            
            tk.Button(
                button_frame,
                text="Connect",
                bg="#000000",
                fg="#33FFFF",
                relief=tk.RAISED,
                command=lambda: self.connect_to_network(network_var.get(), connect_win)
            ).pack(side=tk.LEFT, padx=10)
            
            tk.Button(
                button_frame,
                text="Cancel",
                bg="#000000",
                fg="#FF33A8",
                relief=tk.RAISED,
                command=connect_win.destroy
            ).pack(side=tk.LEFT, padx=10)
    
    def connect_to_network(self, network_name, window):
        """Simulate connecting to a specific network"""
        window.destroy()
        
        # Update status
        self.status_text.config(text=f"Connecting to {network_name.split(' - ')[0]}...")
        
        # Simulate connection
        def connected():
            self.status_text.config(text=f"Connected to {network_name.split(' - ')[0]}!")
            messagebox.showinfo(
                "Connection Established",
                f"Successfully connected to {network_name}!"
            )
        
        self.root.after(1500, connected)
    
    def help_text(self):
        """Show help information"""
        help_win = tk.Toplevel(self.root)
        help_win.title("PNGUIN CYBERDECK HELP")
        help_win.geometry("500x400")
        help_win.configure(bg="#000000")
        help_win.transient(self.root)
        
        # Tab frame
        tab_frame = tk.Frame(help_win, bg="#111111")
        tab_frame.pack(fill=tk.X)
        
        tabs = ["Help", "About", "License", "Contact"]
        for tab in tabs:
            tab_btn = tk.Button(
                tab_frame,
                text=tab,
                bg="#000000",
                fg="#33FFFF",
                relief=tk.RAISED if tab == "Help" else tk.FLAT,
                borderwidth=1,
                font=self.menu_font
            )
            tab_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Help content
        content_frame = tk.Frame(help_win, bg="#000000", relief=tk.SUNKEN, bd=1)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        help_text = """PNGUIN CYBERDECK v1.2
        
        QUICK HELP:
        
        1. Use the buttons on the left sidebar to control the application
        2. "Start Animation" begins animated ASCII art display
        3. "Stop Animation" stops the current animation
        4. Choose between Matrix, Rainbow, and Cyber Wave modes
        5. Use the speed slider to control animation speed
        6. "Connect" simulates connecting to digital networks
        7. Use "Scene Editor" to capture and compile scenes into a GIF
        8. "Ollama Chat" toggles a chat with local LLM models
        9. "Ollama API" for direct single-shot queries
        
        This software runs optimally on:
        - Modern systems with tkinter support
        - Python 3.6 or higher
        - Any operating system with GUI support
        
        (C) 2025 PNGUIN SYSTEMS
        """
        
        help_label = tk.Label(
            content_frame,
            text=help_text,
            font=("Courier", 10),
            bg="#000000",
            fg="#33FFFF",
            justify=tk.LEFT,
            anchor=tk.NW
        )
        help_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def call_ollama_api(self):
        """Call the Ollama API to generate text"""
        # Create dialog to get user input
        ollama_dialog = tk.Toplevel(self.root)
        ollama_dialog.title("Ollama API")
        ollama_dialog.geometry("500x300")
        ollama_dialog.configure(bg="#000000")
        ollama_dialog.transient(self.root)
        ollama_dialog.resizable(True, True)
        
        # Center the dialog
        ollama_dialog.update_idletasks()
        width = ollama_dialog.winfo_width()
        height = ollama_dialog.winfo_height()
        x = (self.root.winfo_rootx() + (self.root.winfo_width() // 2)) - (width // 2)
        y = (self.root.winfo_rooty() + (self.root.winfo_height() // 2)) - (height // 2)
        ollama_dialog.geometry(f"+{x}+{y}")
        
        # Create UI elements
        tk.Label(
            ollama_dialog,
            text="Ollama API Request",
            bg="#000000",
            fg="#FF33FF",
            font=self.title_font
        ).pack(pady=(10, 20))
        
        # Model selection
        model_frame = tk.Frame(ollama_dialog, bg="#000000")
        model_frame.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(
            model_frame,
            text="Model:",
            bg="#000000",
            fg="#33FFFF",
            font=self.menu_font,
            width=10,
            anchor="w"
        ).pack(side=tk.LEFT)
        
        models = ["llama2:7b", "llama2:13b", "llama2:70b"]  # Or any you'd like to list
        model_var = tk.StringVar(ollama_dialog)
        model_var.set(models[0])
        
        model_menu = tk.OptionMenu(model_frame, model_var, *models)
        model_menu.config(bg="#111111", fg="#33FFFF", width=15)
        model_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Prompt entry
        prompt_frame = tk.Frame(ollama_dialog, bg="#000000")
        prompt_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        tk.Label(
            prompt_frame,
            text="Prompt:",
            bg="#000000",
            fg="#33FFFF",
            font=self.menu_font,
            anchor="nw",
            justify=tk.LEFT
        ).pack(anchor="w")
        
        prompt_text = tk.Text(
            prompt_frame,
            height=5,
            bg="#111111",
            fg="#33FFFF",
            insertbackground="#33FFFF",
            relief=tk.SUNKEN,
            font=self.status_font
        )
        prompt_text.pack(fill=tk.BOTH, expand=True, pady=5)
        prompt_text.insert(tk.END, "Generate ASCII art of a retro computer")
        
        # Button frame
        button_frame = tk.Frame(ollama_dialog, bg="#000000")
        button_frame.pack(fill=tk.X, padx=20, pady=(5, 10))
        
        def send_request():
            model = model_var.get()
            prompt = prompt_text.get("1.0", tk.END).strip()
            
            if not prompt:
                messagebox.showwarning("Input Required", "Please enter a prompt")
                return
                
            # Update status
            self.status_text.config(text=f"Sending request to Ollama API ({model})...")
            ollama_dialog.destroy()
            
            # Start a thread to handle the API request
            threading.Thread(
                target=self._ollama_api_thread,
                args=(model, prompt),
                daemon=True
            ).start()
        
        tk.Button(
            button_frame,
            text="Send",
            bg="#111111",
            fg="#33FFFF",
            font=self.menu_font,
            command=send_request,
            width=10
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="Cancel",
            bg="#111111",
            fg="#FF33A8",
            font=self.menu_font,
            command=ollama_dialog.destroy,
            width=10
        ).pack(side=tk.LEFT)
        
        # Make dialog modal
        ollama_dialog.grab_set()
        self.root.wait_window(ollama_dialog)
    
    def _ollama_api_thread(self, model, prompt):
        """Thread to handle Ollama API request to /api/generate (single-shot)"""
        try:
            api_url = "http://localhost:11434/api/generate"
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False
            }
            
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                result = data.get('response', 'No response received')
                self.root.after(0, lambda: self._display_ollama_result(result))
            else:
                error_msg = f"Error: API returned status code {response.status_code}"
                self.root.after(0, lambda: self.status_text.config(text=error_msg))
                self.root.after(0, lambda: messagebox.showerror("API Error", error_msg))
                
        except Exception as e:
            error_msg = f"Error communicating with Ollama API: {str(e)}"
            self.root.after(0, lambda: self.status_text.config(text=error_msg))
            self.root.after(0, lambda: messagebox.showerror("API Error", error_msg))
    
    def _display_ollama_result(self, result):
        """Display the result from Ollama API in a dialog"""
        result_dialog = tk.Toplevel(self.root)
        result_dialog.title("Ollama API Result")
        result_dialog.geometry("600x400")
        result_dialog.configure(bg="#000000")
        result_dialog.transient(self.root)
        
        tk.Label(
            result_dialog,
            text="API Response",
            bg="#000000",
            fg="#FF33FF",
            font=self.title_font
        ).pack(pady=(10, 5))
        
        result_frame = tk.Frame(result_dialog, bg="#000000")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        scrollbar_y = tk.Scrollbar(result_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = tk.Scrollbar(result_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        result_text = tk.Text(
            result_frame,
            bg="#111111",
            fg="#33FFFF",
            font=("Courier", 10),
            wrap=tk.NONE,
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set
        )
        result_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar_y.config(command=result_text.yview)
        scrollbar_x.config(command=result_text.xview)
        
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)
        
        button_frame = tk.Frame(result_dialog, bg="#000000")
        button_frame.pack(fill=tk.X, pady=10)
        
        def use_as_ascii():
            content = result
            self.canvas.delete("all")
            self.canvas.create_text(
                self.canvas.winfo_width() // 2,
                self.canvas.winfo_height() // 2,
                text=content,
                font=self.ascii_font,
                fill=random.choice(self.COLORS),
                tags="ascii"
            )
            self.status_text.config(text="Ollama-generated content displayed")
            result_dialog.destroy()
        
        tk.Button(
            button_frame,
            text="Use as ASCII Art",
            bg="#111111",
            fg="#33FFFF",
            command=use_as_ascii
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="Close",
            bg="#111111",
            fg="#FF33A8",
            command=result_dialog.destroy
        ).pack(side=tk.RIGHT, padx=10)
        
        self.status_text.config(text="Received response from Ollama API")

    # -------------------------------------------------------------------------
    # OLLAMA CHAT SIDEBAR METHODS
    # -------------------------------------------------------------------------
    def open_ollama_chat(self):
        """Toggle the Ollama chat sidebar on the right"""
        if not self.ollama_chat_open:
            # Fetch the available models
            self.fetch_ollama_models()
            
            # Show the ollama chat sidebar
            self.ollama_chat_sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
            self.ollama_chat_open = True
            self.status_text.config(text="Ollama chat opened. Chat with your local models.")
        else:
            # Hide the ollama chat sidebar
            self.ollama_chat_sidebar.pack_forget()
            self.ollama_chat_open = False
            self.status_text.config(text="Ollama chat closed.")
    
    def fetch_ollama_models(self):
        """Retrieve local models from /api/tags and update the dropdown"""
        try:
            api_url = "http://localhost:11434/api/tags"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                models = data.get("models", [])
                # The 'model' key in each entry might be something like "llama2:7b"
                # We'll collect them in a list
                self.ollama_available_models = [m["model"] for m in models if "model" in m]
                
                if not self.ollama_available_models:
                    self.ollama_available_models = ["llama2:7b"]  # Fallback
                
            else:
                # If there's an error, just set a fallback
                self.ollama_available_models = ["llama2:7b", "llama2:13b"]
            
            # Update the dropdown
            menu = self.ollama_model_dropdown["menu"]
            menu.delete(0, "end")
            for model_name in self.ollama_available_models:
                menu.add_command(label=model_name, command=lambda v=model_name: self.ollama_model_var.set(v))
            # Set a default
            self.ollama_model_var.set(self.ollama_available_models[0])
            
        except Exception as e:
            messagebox.showerror("Ollama Model Fetch Error", f"Failed to fetch local models: {str(e)}")
            self.ollama_available_models = ["llama2:7b"]
            self.ollama_model_var.set("llama2:7b")
    
    def ollama_send_message(self):
        """Send the user's message to the Ollama chat endpoint (/api/chat)"""
        user_msg = self.ollama_chat_entry.get().strip()
        if not user_msg:
            return
        
        self.ollama_chat_entry.delete(0, tk.END)
        
        # Append the user message to the conversation
        self.ollama_chat_messages.append({"role": "user", "content": user_msg})
        
        # Display the user message
        self.display_chat_message("User", user_msg)
        
        # Send the chat to Ollama
        threading.Thread(target=self._ollama_chat_thread, daemon=True).start()
    
    def _ollama_chat_thread(self):
        """Worker thread to call the /api/chat endpoint with the full conversation"""
        self.status_text.config(text="Contacting Ollama chat endpoint...")
        # Construct the messages with a system prompt at the start
        messages_payload = [
            {"role": "system", "content": self.ollama_system_prompt}
        ]
        messages_payload.extend(self.ollama_chat_messages)
        
        selected_model = self.ollama_model_var.get() or "llama2:7b"
        payload = {
            "model": selected_model,
            "messages": messages_payload,
            "stream": False
        }
        
        try:
            api_url = "http://localhost:11434/api/chat"
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # The server returns a final assistant message in 'response'
                assistant_msg = data.get("response", "")
                if assistant_msg:
                    self.ollama_chat_messages.append({"role": "assistant", "content": assistant_msg})
                    # Update the chat display
                    self.root.after(0, lambda: self.display_chat_message("Assistant", assistant_msg))
                    self.root.after(0, lambda: self.status_text.config(text="Assistant responded."))
            else:
                error_msg = f"Ollama chat error: {response.status_code}"
                self.root.after(0, lambda: messagebox.showerror("Chat Error", error_msg))
                self.root.after(0, lambda: self.status_text.config(text=error_msg))
        except Exception as e:
            error_msg = f"Ollama chat request failed: {str(e)}"
            self.root.after(0, lambda: messagebox.showerror("Chat Error", error_msg))
            self.root.after(0, lambda: self.status_text.config(text=error_msg))
    
    def display_chat_message(self, sender, message):
        """Append a message to the chat text display"""
        self.ollama_chat_text.config(state=tk.NORMAL)
        self.ollama_chat_text.insert(tk.END, f"{sender}: {message}\n\n")
        self.ollama_chat_text.config(state=tk.DISABLED)
        self.ollama_chat_text.see(tk.END)
    
    # -------------------------------------------------------------------------
    
    def exit_app(self):
        """Exit the application with a confirmation dialog"""
        exit_dialog = tk.Toplevel(self.root)
        exit_dialog.title("Exit Confirmation")
        exit_dialog.geometry("350x150")
        exit_dialog.configure(bg="#000000")
        exit_dialog.transient(self.root)
        exit_dialog.resizable(False, False)
        
        # Center the dialog
        exit_dialog.update_idletasks()
        width = exit_dialog.winfo_width()
        height = exit_dialog.winfo_height()
        x = (self.root.winfo_rootx() + (self.root.winfo_width() // 2)) - (width // 2)
        y = (self.root.winfo_rooty() + (self.root.winfo_height() // 2)) - (height // 2)
        exit_dialog.geometry(f"+{x}+{y}")
        
        tk.Label(
            exit_dialog,
            text="Are you sure you want to exit?\nAll unsaved ASCII art will be lost!",
            bg="#000000",
            fg="#FF33A8",
            font=self.menu_font
        ).pack(pady=20)
        
        btn_frame = tk.Frame(exit_dialog, bg="#000000")
        btn_frame.pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="Yes",
            bg="#000000",
            fg="#33FFFF",
            command=lambda: self.confirm_exit(exit_dialog),
            width=10
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame,
            text="No",
            bg="#000000",
            fg="#FF33A8",
            command=exit_dialog.destroy,
            width=10
        ).pack(side=tk.LEFT, padx=10)
        
        # Make dialog modal
        exit_dialog.grab_set()
        self.root.wait_window(exit_dialog)
    
    def confirm_exit(self, dialog):
        """Confirm and execute the exit"""
        dialog.destroy()
        
        # Simulate disconnecting
        if self.modem_connected:
            self.status_text.config(text="Disconnecting from network...")
            self.connection_indicator.config(text="⚫ OFFLINE", fg="#FF33A8")
            self.root.update()
            time.sleep(0.5)
        
        self.root.destroy()


def main():
    """Main function to start the application"""
    root = tk.Tk()
    app = RadRainbowASCII(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_app)  # Proper handling of window close
    root.mainloop()


if __name__ == "__main__":
    main()
