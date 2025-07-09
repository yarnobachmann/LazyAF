import customtkinter as ctk
import pyautogui
import threading
import time
import random
import json
import os
from pynput import mouse, keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import tkinter as tk
from tkinter import messagebox

class AutoClicker:
    def __init__(self):
        # Configure CustomTkinter appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("LazyAF 4.20 - Professional Dashboard")
        self.root.geometry("1000x900")
        self.root.resizable(True, True)
        self.root.minsize(950, 850)
        
        # Ultra-modern sleek color scheme
        self.colors = {
            "primary": "#6366f1",       # Modern indigo
            "secondary": "#8b5cf6",     # Vibrant purple  
            "accent": "#06b6d4",        # Cyan accent
            "warning": "#fbbf24",       # Amber warning
            "danger": "#ef4444",        # Clean red
            "success": "#10b981",       # Emerald green
            "bg_dark": "#0f172a",       # Slate 900
            "bg_light": "#1e293b",      # Slate 800
            "bg_card": "#334155",       # Slate 700
            "text_primary": "#f8fafc",  # Pure white
            "text_secondary": "#94a3b8", # Slate 400
            "button_hover": "#4f46e5",  # Indigo hover
            "gradient_start": "#6366f1", # Gradient colors
            "gradient_end": "#8b5cf6"
        }
        
        # Application state
        self.clicking = False
        self.click_thread = None
        self.position_picking = False
        self.selected_position = (0, 0)
        self.position_listener = None
        self.hotkey_listener = None
        self.start_hotkey = None
        self.stop_hotkey = None
        
        # Variables
        self.hours_var = ctk.StringVar(value="0")
        self.minutes_var = ctk.StringVar(value="0") 
        self.seconds_var = ctk.StringVar(value="0")
        self.milliseconds_var = ctk.StringVar(value="100")
        self.random_offset_var = ctk.BooleanVar()
        self.random_offset_value_var = ctk.StringVar(value="40")
        self.mouse_button_var = ctk.StringVar(value="Left")
        self.click_type_var = ctk.StringVar(value="Single")
        self.repeat_mode_var = ctk.StringVar(value="until_stopped")
        self.repeat_count_var = ctk.StringVar(value="1")
        self.position_mode_var = ctk.StringVar(value="current")
        self.x_pos_var = ctk.StringVar(value="0")
        self.y_pos_var = ctk.StringVar(value="0")
        self.click_target_var = ctk.StringVar(value="mouse")
        self.keyboard_key_var = ctk.StringVar(value="space")
        self.automation_mode_var = ctk.StringVar(value="🖱️ Mouse")  # "🖱️ Mouse" or "⌨️ Keyboard"
        self.key_capture_mode = False
        self.key_capture_listener = None
        
        # Settings file path
        self.settings_file = "lazyaf_settings.json"
        
        self.setup_ui()
        self.load_settings()
        
    def setup_ui(self):
        # Configure main frame with full-screen styling (no margins)
        main_frame = ctk.CTkFrame(self.root, fg_color=self.colors["bg_dark"])
        main_frame.pack(fill="both", expand=True)
        
        # Settings Topbar
        settings_topbar = ctk.CTkFrame(main_frame, fg_color=self.colors["bg_card"], height=50)
        settings_topbar.pack(fill="x", padx=15, pady=(15, 0))
        settings_topbar.pack_propagate(False)
        
        # Settings topbar content
        topbar_content = ctk.CTkFrame(settings_topbar, fg_color="transparent")
        topbar_content.pack(fill="both", expand=True, padx=20, pady=8)
        
        # Left side - Settings menu
        settings_menu = ctk.CTkFrame(topbar_content, fg_color="transparent")
        settings_menu.pack(side="left", fill="y")
        
        ctk.CTkLabel(
            settings_menu,
            text="Settings:",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.colors["text_secondary"]
        ).pack(side="left", padx=(0, 15))
        
        # Settings buttons with clear labels
        ctk.CTkButton(
            settings_menu,
            text="Save",
            command=self.save_settings,
            fg_color=self.colors["success"],
            hover_color="#059669",
            text_color="white",
            font=ctk.CTkFont(size=11, weight="bold"),
            width=60,
            height=32,
            corner_radius=6
        ).pack(side="left", padx=(0, 8))
        
        ctk.CTkButton(
            settings_menu,
            text="Load",
            command=self.load_settings,
            fg_color=self.colors["primary"],
            hover_color=self.colors["button_hover"],
            text_color="white",
            font=ctk.CTkFont(size=11, weight="bold"),
            width=60,
            height=32,
            corner_radius=6
        ).pack(side="left", padx=(0, 8))
        
        ctk.CTkButton(
            settings_menu,
            text="Reset",
            command=self.reset_settings,
            fg_color=self.colors["danger"],
            hover_color="#dc2626",
            text_color="white",
            font=ctk.CTkFont(size=11, weight="bold"),
            width=60,
            height=32,
            corner_radius=6
        ).pack(side="left", padx=(0, 8))
        
        ctk.CTkButton(
            settings_menu,
            text="Hotkeys",
            command=self.setup_hotkeys,
            fg_color=self.colors["secondary"],
            hover_color="#7c3aed",
            text_color="white",
            font=ctk.CTkFont(size=11, weight="bold"),
            width=70,
            height=32,
            corner_radius=6
        ).pack(side="left")
        
        # Right side - Action buttons
        action_section = ctk.CTkFrame(topbar_content, fg_color="transparent")
        action_section.pack(side="right", fill="y")
        
        ctk.CTkLabel(
            action_section,
            text="Controls:",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.colors["text_secondary"]
        ).pack(side="left", padx=(0, 15))
        
        # Start button
        self.start_button = ctk.CTkButton(
            action_section,
            text="▶️ Start",
            command=self.toggle_clicking,
            fg_color=self.colors["success"],
            hover_color="#059669",
            text_color="white",
            font=ctk.CTkFont(size=12, weight="bold"),
            width=90,
            height=32,
            corner_radius=6
        )
        self.start_button.pack(side="left", padx=(0, 8))
        
        # Stop button
        self.stop_button = ctk.CTkButton(
            action_section,
            text="⏹️ Stop",
            command=self.stop_clicking,
            fg_color=self.colors["danger"],
            hover_color="#dc2626",
            text_color="white",
            font=ctk.CTkFont(size=12, weight="bold"),
            width=90,
            height=32,
            corner_radius=6,
            state="disabled"
        )
        self.stop_button.pack(side="left")
        
        # Header with title
        header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(20, 25))
        
        # Centered title
        title_label = ctk.CTkLabel(
            header_frame, 
            text="LazyAF 4.20",
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=self.colors["text_primary"]
        )
        title_label.pack()
        
        # Dashboard grid container
        dashboard_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        dashboard_frame.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        
        # Configure grid layout (3x2 dashboard) with consistent spacing
        for i in range(3):
            dashboard_frame.grid_columnconfigure(i, weight=1, uniform="col")
        for i in range(2):
            dashboard_frame.grid_rowconfigure(i, weight=1, uniform="row")
        
        # Setup dashboard cards
        self.setup_dashboard_cards(dashboard_frame)
        
        # Control panel at bottom
        self.setup_control_panel(main_frame)
        
        # Initialize key display
        self.update_key_display()

    def setup_dashboard_cards(self, parent):
        """Setup all dashboard cards in a unified layout"""
        
        # Row 1: Mouse Configuration Cards
        # Top Left: Timing Card
        timing_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        timing_card.grid(row=0, column=0, padx=(0, 6), pady=(0, 6), sticky="nsew")
        
        ctk.CTkLabel(timing_card, text="⏱️ Click Timing", font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Timing inputs in compact layout
        time_grid = ctk.CTkFrame(timing_card, fg_color="transparent")
        time_grid.pack(padx=15, pady=(0, 10))
        
        # First row: Hours and Minutes
        ctk.CTkLabel(time_grid, text="Hours", text_color=self.colors["text_secondary"], 
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, pady=(0, 3))
        ctk.CTkEntry(time_grid, textvariable=self.hours_var, width=60, height=30,
                    border_color=self.colors["primary"], font=ctk.CTkFont(size=12)).grid(row=1, column=0, padx=(0, 8))
        
        ctk.CTkLabel(time_grid, text="Minutes", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, pady=(0, 3))
        ctk.CTkEntry(time_grid, textvariable=self.minutes_var, width=60, height=30,
                    border_color=self.colors["primary"], font=ctk.CTkFont(size=12)).grid(row=1, column=1, padx=(0, 15))
        
        # Second row: Seconds and Milliseconds  
        ctk.CTkLabel(time_grid, text="Seconds", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=2, pady=(0, 3))
        ctk.CTkEntry(time_grid, textvariable=self.seconds_var, width=60, height=30,
                    border_color=self.colors["primary"], font=ctk.CTkFont(size=12)).grid(row=1, column=2, padx=(0, 8))
        
        ctk.CTkLabel(time_grid, text="Milliseconds", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=3, pady=(0, 3))
        ctk.CTkEntry(time_grid, textvariable=self.milliseconds_var, width=75, height=30,
                    border_color=self.colors["primary"], font=ctk.CTkFont(size=12)).grid(row=1, column=3)
        
        # Random offset
        offset_frame = ctk.CTkFrame(timing_card, fg_color="transparent")
        offset_frame.pack(pady=(8, 8))
        
        ctk.CTkCheckBox(offset_frame, text="Random Offset ±", variable=self.random_offset_var,
                       text_color=self.colors["text_primary"], fg_color=self.colors["secondary"],
                       font=ctk.CTkFont(size=12)).pack(side="left")
        ctk.CTkEntry(offset_frame, textvariable=self.random_offset_value_var, width=60, height=30,
                    border_color=self.colors["secondary"], font=ctk.CTkFont(size=12)).pack(side="left", padx=(8, 5))
        ctk.CTkLabel(offset_frame, text="ms", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12)).pack(side="left")
        
        # Safety notice - moved from Mouse Options
        safety_frame = ctk.CTkFrame(timing_card, fg_color=self.colors["warning"], corner_radius=6)
        safety_frame.pack(fill="x", padx=15, pady=(5, 15))
        ctk.CTkLabel(safety_frame, text="⚠️ Minimum Interval: 10ms", text_color="black",
                    font=ctk.CTkFont(size=11, weight="bold")).pack(pady=4)
        
        # Top Middle: Mouse Options Card
        options_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        options_card.grid(row=0, column=1, padx=(3, 3), pady=(0, 6), sticky="nsew")
        
        ctk.CTkLabel(options_card, text="🖱️ Mouse Options", font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Mouse button selection
        button_frame = ctk.CTkFrame(options_card, fg_color="transparent")
        button_frame.pack(pady=8)
        ctk.CTkLabel(button_frame, text="Mouse Button", text_color=self.colors["text_secondary"], 
                    font=ctk.CTkFont(size=12, weight="bold")).pack(pady=(0, 5))
        mouse_button_menu = ctk.CTkOptionMenu(button_frame, variable=self.mouse_button_var,
                                            values=["Left", "Right", "Middle"], width=130, height=32,
                                            fg_color=self.colors["primary"], font=ctk.CTkFont(size=12))
        mouse_button_menu.pack()
        
        # Click type selection
        type_frame = ctk.CTkFrame(options_card, fg_color="transparent")
        type_frame.pack(pady=8)
        ctk.CTkLabel(type_frame, text="Click Type", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).pack(pady=(0, 5))
        click_type_menu = ctk.CTkOptionMenu(type_frame, variable=self.click_type_var,
                                          values=["Single", "Double"], width=130, height=32,
                                          fg_color=self.colors["primary"], font=ctk.CTkFont(size=12))
        click_type_menu.pack()
        
        # Modern info panel
        info_panel = ctk.CTkFrame(options_card, fg_color=self.colors["bg_light"], corner_radius=6)
        info_panel.pack(fill="x", padx=15, pady=(10, 15))
        ctk.CTkLabel(info_panel, text="💡 Mouse click automation", text_color=self.colors["text_primary"],
                    font=ctk.CTkFont(size=11, weight="bold")).pack(pady=6)
        
        # Top Right: Position Card
        position_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        position_card.grid(row=0, column=2, padx=(6, 0), pady=(0, 6), sticky="nsew")
        
        ctk.CTkLabel(position_card, text="📍 Click Position", font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Position mode selection with better alignment
        position_modes_frame = ctk.CTkFrame(position_card, fg_color="transparent")
        position_modes_frame.pack(pady=8)
        
        ctk.CTkRadioButton(position_modes_frame, text="Current cursor", variable=self.position_mode_var,
                          value="current", text_color=self.colors["text_primary"],
                          fg_color=self.colors["accent"], font=ctk.CTkFont(size=12)).pack(anchor="w", pady=3)
        
        ctk.CTkRadioButton(position_modes_frame, text="Pick coordinates", variable=self.position_mode_var,
                          value="pick", text_color=self.colors["text_primary"],
                          fg_color=self.colors["accent"], font=ctk.CTkFont(size=12)).pack(anchor="w", pady=3)
        
        # Pick location button
        pick_button = ctk.CTkButton(position_card, text="📍 Pick", command=self.pick_location,
                                   fg_color=self.colors["accent"], width=120, height=32,
                                   font=ctk.CTkFont(size=12, weight="bold"))
        pick_button.pack(pady=10)
        
        # Coordinates display
        coord_frame = ctk.CTkFrame(position_card, fg_color="transparent")
        coord_frame.pack(pady=(8, 15))
        
        ctk.CTkLabel(coord_frame, text="X", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, padx=(0, 8))
        ctk.CTkEntry(coord_frame, textvariable=self.x_pos_var, width=60, height=30,
                    border_color=self.colors["accent"], font=ctk.CTkFont(size=12)).grid(row=1, column=0, padx=(0, 8))
        
        ctk.CTkLabel(coord_frame, text="Y", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1)
        ctk.CTkEntry(coord_frame, textvariable=self.y_pos_var, width=60, height=30,
                    border_color=self.colors["accent"], font=ctk.CTkFont(size=12)).grid(row=1, column=1)
        
        # Row 2: Repeat & Keyboard Cards
        # Bottom Left: Repeat Settings Card
        repeat_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        repeat_card.grid(row=1, column=0, padx=(0, 6), pady=(3, 0), sticky="nsew")
        
        ctk.CTkLabel(repeat_card, text="🔄 Repeat Settings", font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Repeat options with better alignment
        repeat_options_frame = ctk.CTkFrame(repeat_card, fg_color="transparent")
        repeat_options_frame.pack(pady=8, padx=10)
        
        # Count option with aligned entry
        count_option_frame = ctk.CTkFrame(repeat_options_frame, fg_color="transparent")
        count_option_frame.pack(fill="x", pady=3)
        
        ctk.CTkRadioButton(count_option_frame, text="Count:", variable=self.repeat_mode_var, value="repeat",
                          text_color=self.colors["text_primary"], fg_color=self.colors["secondary"],
                          font=ctk.CTkFont(size=12)).pack(anchor="w")
        
        count_frame = ctk.CTkFrame(count_option_frame, fg_color="transparent")
        count_frame.pack(anchor="w", pady=(5, 0))
        ctk.CTkEntry(count_frame, textvariable=self.repeat_count_var, width=80, height=30,
                    border_color=self.colors["secondary"], font=ctk.CTkFont(size=12)).pack(side="left", padx=(20, 8))
        ctk.CTkLabel(count_frame, text="times", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12)).pack(side="left")
        
        # Until stopped option
        ctk.CTkRadioButton(repeat_options_frame, text="Until stopped", variable=self.repeat_mode_var,
                          value="until_stopped", text_color=self.colors["text_primary"],
                          fg_color=self.colors["secondary"], font=ctk.CTkFont(size=12)).pack(anchor="w", pady=(12, 0))
        
        # Add spacing at bottom
        ctk.CTkFrame(repeat_card, fg_color="transparent", height=10).pack()
        
        # Bottom Center: Keyboard Card
        keyboard_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        keyboard_card.grid(row=1, column=1, padx=(3, 3), pady=(3, 0), sticky="nsew")
        
        ctk.CTkLabel(keyboard_card, text="⌨️ Keyboard", 
                    font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Current key display
        display_frame = ctk.CTkFrame(keyboard_card, fg_color="transparent")
        display_frame.pack(pady=8)
        
        ctk.CTkLabel(display_frame, text="Selected Key:", text_color=self.colors["text_secondary"],
                    font=ctk.CTkFont(size=12, weight="bold")).pack(pady=(0, 5))
        
        self.key_display = ctk.CTkLabel(display_frame, text=self.keyboard_key_var.get(),
                                       font=ctk.CTkFont(size=16, weight="bold"),
                                       text_color=self.colors["text_primary"],
                                       fg_color=self.colors["secondary"],
                                       corner_radius=6, width=80, height=32)
        self.key_display.pack()
        
        # Key selection methods
        methods_frame = ctk.CTkFrame(keyboard_card, fg_color="transparent")
        methods_frame.pack(pady=10)
        
        # Capture method
        self.key_capture_button = ctk.CTkButton(methods_frame, text="🎯 Capture",
                                               command=self.start_key_capture, fg_color=self.colors["secondary"],
                                               width=100, height=32, font=ctk.CTkFont(size=12, weight="bold"))
        self.key_capture_button.pack(pady=3)
        
        # Quick select method
        key_menu = ctk.CTkOptionMenu(methods_frame, variable=self.keyboard_key_var,
                                   values=["space", "enter", "tab", "shift", "ctrl", "alt", "a", "s", "d", "w", "1", "2", "3", "4", "5"],
                                   fg_color=self.colors["primary"], command=self.update_key_display,
                                   width=100, height=32, font=ctk.CTkFont(size=12))
        key_menu.pack(pady=(3, 15))
        
        # Bottom Right: Status & Info Card
        info_card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=12)
        info_card.grid(row=1, column=2, padx=(6, 0), pady=(3, 0), sticky="nsew")
        
        ctk.CTkLabel(info_card, text="📊 System Status",
                    font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 10))
        
        # Status display
        self.status_label = ctk.CTkLabel(
            info_card,
            text="Ready to start automation",
            font=ctk.CTkFont(size=12),
            text_color=self.colors["text_secondary"],
            wraplength=200
        )
        self.status_label.pack(pady=10)
        
        # Info section
        info_text_frame = ctk.CTkFrame(info_card, fg_color=self.colors["bg_light"], corner_radius=6)
        info_text_frame.pack(fill="x", padx=15, pady=(8, 15))
        
        ctk.CTkLabel(info_text_frame, text="ℹ️ Quick Info",
                    font=ctk.CTkFont(size=12, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(10, 5))
        
        ctk.CTkLabel(info_text_frame, text="• DEL key: Start/Stop\n• Same timing for both modes\n• Min interval: 10ms\n• Failsafe enabled",
                    font=ctk.CTkFont(size=10), text_color=self.colors["text_secondary"],
                    justify="left").pack(pady=(0, 10))

    def setup_control_panel(self, parent):
        """Setup the mode selection panel"""
        control_frame = ctk.CTkFrame(parent, fg_color=self.colors["bg_dark"], corner_radius=12)
        control_frame.pack(fill="x", padx=15, pady=(5, 15))
        
        # Main controls section
        main_controls = ctk.CTkFrame(control_frame, fg_color="transparent")
        main_controls.pack(fill="x", padx=20, pady=15)
        
        # Prominent mode selector with clear selection required
        mode_container = ctk.CTkFrame(main_controls, fg_color=self.colors["bg_card"], corner_radius=12)
        mode_container.pack(pady=0, padx=100, fill="x")
        
        # Clear instruction with emphasis
        mode_instruction = ctk.CTkFrame(mode_container, fg_color=self.colors["accent"], corner_radius=8)
        mode_instruction.pack(fill="x", padx=15, pady=(12, 8))
        
        ctk.CTkLabel(
            mode_instruction,
            text="⚡ SELECT AUTOMATION MODE ⚡",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="black"
        ).pack(pady=6)
        
        mode_selector = ctk.CTkSegmentedButton(
            mode_container,
            values=["🖱️ Mouse", "⌨️ Keyboard"],
            variable=self.automation_mode_var,
            font=ctk.CTkFont(size=13, weight="bold"),
            height=42,
            fg_color=self.colors["bg_light"],
            selected_color=self.colors["secondary"],
            selected_hover_color="#7c3aed",
            unselected_color=self.colors["bg_light"],
            unselected_hover_color=self.colors["primary"]
        )
        mode_selector.pack(pady=(0, 15), padx=20)
        
        # Setup default hotkeys
        self.setup_default_hotkeys()
    

        

        
    def get_click_interval(self):
        """Calculate total click interval in seconds"""
        try:
            hours = int(self.hours_var.get() or 0)
            minutes = int(self.minutes_var.get() or 0)
            seconds = int(self.seconds_var.get() or 0)
            milliseconds = int(self.milliseconds_var.get() or 0)
            
            total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000.0
            
            # Check if interval is too fast
            if total_seconds < 0.01:
                self.status_label.configure(text="⚠️ Interval too fast! Using minimum 10ms")
                total_seconds = 0.01
            
            if self.random_offset_var.get():
                offset = int(self.random_offset_value_var.get() or 0) / 1000.0
                total_seconds += random.uniform(-offset, offset)
                
            return max(0.01, total_seconds)  # Minimum 10ms for safety
        except ValueError:
            return 0.1  # Default 100ms
    
    def pick_location(self):
        """Allow user to pick a location by clicking"""
        if self.position_picking:
            return
            
        self.position_picking = True
        self.status_label.configure(text="Click anywhere to pick location...")
        
        def on_click(x, y, button, pressed):
            if pressed and self.position_picking:
                try:
                    self.selected_position = (x, y)
                    self.x_pos_var.set(str(x))
                    self.y_pos_var.set(str(y))
                    self.position_picking = False
                    
                    # Update UI from main thread
                    self.root.after(0, lambda: self.status_label.configure(text=f"Location picked: ({x}, {y})"))
                    
                    # Stop the listener
                    if hasattr(self, 'position_listener') and self.position_listener:
                        self.position_listener.stop()
                    
                    return False  # Stop listener
                except Exception as e:
                    print(f"Position picking error: {e}")
                    self.position_picking = False
                    self.root.after(0, lambda: self.status_label.configure(text="Position picking failed"))
                    return False
        
        try:
            # Start mouse listener
            self.position_listener = MouseListener(on_click=on_click)
            self.position_listener.daemon = True
            self.position_listener.start()
        except Exception as e:
            print(f"Failed to start position listener: {e}")
            self.position_picking = False
            self.status_label.configure(text="Position picking failed to start")
    
    def perform_click(self):
        """Perform a single click or key press action"""
        try:
            automation_mode = self.automation_mode_var.get()
            
            if automation_mode == "mouse" or "Mouse" in automation_mode:
                # Mouse click action
                # Get position
                if self.position_mode_var.get() == "current":
                    x, y = pyautogui.position()
                else:
                    x = int(self.x_pos_var.get() or 0)
                    y = int(self.y_pos_var.get() or 0)
                
                # Get button
                button_map = {"Left": "left", "Right": "right", "Middle": "middle"}
                button = button_map[self.mouse_button_var.get()]
                
                # Perform click
                if self.click_type_var.get() == "Double":
                    pyautogui.doubleClick(x, y, button=button)
                else:
                    pyautogui.click(x, y, button=button)
            
            elif automation_mode == "keyboard" or "Keyboard" in automation_mode:
                # Keyboard press action
                key = self.keyboard_key_var.get()
                pyautogui.press(key)
                
        except Exception as e:
            print(f"Action error: {e}")
    
    def click_worker(self):
        """Worker thread for clicking"""
        click_count = 0
        max_clicks = None
        
        if self.repeat_mode_var.get() == "repeat":
            try:
                max_clicks = int(self.repeat_count_var.get() or 1)
            except ValueError:
                max_clicks = 1
        
        while self.clicking:
            try:
                self.perform_click()
                click_count += 1
                
                # Update status
                if max_clicks:
                    self.status_label.configure(text=f"🔄 Automating... ({click_count}/{max_clicks})")
                    if click_count >= max_clicks:
                        break
                else:
                    self.status_label.configure(text=f"🔄 Automating... ({click_count} actions)")
                
                # Wait for next click
                interval = self.get_click_interval()
                time.sleep(interval)
                
            except Exception as e:
                print(f"Click worker error: {e}")
                break
        
        # Reset state
        self.clicking = False
        self.root.after(0, self.update_ui_after_stop)
    
    def toggle_clicking(self):
        """Start or stop clicking"""
        if not self.clicking:
            self.start_clicking()
        else:
            self.stop_clicking()
    
    def start_clicking(self):
        """Start the clicking process"""
        if self.clicking:
            return
            
        self.clicking = True
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        
        # Start clicking thread
        self.click_thread = threading.Thread(target=self.click_worker, daemon=True)
        self.click_thread.start()
    
    def stop_clicking(self):
        """Stop the clicking process"""
        self.clicking = False
    
    def update_ui_after_stop(self):
        """Update UI after stopping"""
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.status_label.configure(text="⏹️ Automation stopped")
    
    def setup_hotkeys(self):
        """Setup custom hotkeys"""
        hotkey_window = ctk.CTkToplevel(self.root)
        hotkey_window.title("Hotkey Configuration")
        hotkey_window.geometry("380x280")
        hotkey_window.grab_set()
        
        # Main frame
        main_frame = ctk.CTkFrame(hotkey_window, fg_color=self.colors["bg_card"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(main_frame, text="⌨️ Hotkey Configuration", 
                    font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(20, 15))
        
        # Info section
        info_frame = ctk.CTkFrame(main_frame, fg_color=self.colors["bg_light"], corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        ctk.CTkLabel(info_frame, text="Current Hotkey Configuration:",
                    font=ctk.CTkFont(size=14, weight="bold"),
                    text_color=self.colors["text_primary"]).pack(pady=(15, 5))
        
        ctk.CTkLabel(info_frame, text="🔹 DEL key: Start/Stop automation\n🔹 Works globally (even when minimized)\n🔹 Mouse corner: Emergency stop",
                    text_color=self.colors["text_secondary"],
                    justify="left").pack(pady=(0, 15))
        
        # Button frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=(0, 20))
        
        ctk.CTkButton(button_frame, text="✅ Got it", command=hotkey_window.destroy,
                     fg_color=self.colors["primary"], hover_color=self.colors["primary"],
                     text_color="white", width=120, height=35).pack()
    
    def setup_default_hotkeys(self):
        """Setup default DEL key hotkey"""
        def on_press(key):
            try:
                if key == Key.delete:
                    self.root.after(0, self.toggle_clicking)
            except:
                pass
        
        def on_release(key):
            pass
        
        # Start hotkey listener
        self.hotkey_listener = KeyboardListener(on_press=on_press, on_release=on_release)
        self.hotkey_listener.daemon = True
        self.hotkey_listener.start()
    
    def run(self):
        """Run the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def start_key_capture(self):
        """Start capturing a key press"""
        if self.key_capture_mode:
            return
            
        self.key_capture_mode = True
        self.key_capture_button.configure(text="🎯 Press any key...", fg_color=self.colors["warning"])
        self.status_label.configure(text="Waiting for key press...")
        
        def on_key_press(key):
            if self.key_capture_mode:
                try:
                    # Handle special keys
                    if hasattr(key, 'name'):
                        key_name = key.name
                    elif hasattr(key, 'char') and key.char:
                        key_name = key.char.lower()
                    else:
                        key_name = str(key).replace("'", "").replace("Key.", "")
                    
                    # Set the captured key
                    self.keyboard_key_var.set(key_name)
                    self.update_key_display()
                    
                    # Stop capture mode
                    self.key_capture_mode = False
                    self.key_capture_button.configure(text="🎯 Capture Key Press", fg_color=self.colors["secondary"])
                    self.status_label.configure(text=f"✅ Key captured: {key_name}")
                    
                    return False  # Stop listener
                except Exception as e:
                    print(f"Key capture error: {e}")
                    self.key_capture_mode = False
                    self.key_capture_button.configure(text="🎯 Capture Key Press", fg_color=self.colors["secondary"])
                    self.status_label.configure(text="❌ Key capture failed")
                    return False
        
        # Start temporary key listener
        self.key_capture_listener = KeyboardListener(on_press=on_key_press)
        self.key_capture_listener.daemon = True
        self.key_capture_listener.start()
    
    def update_key_display(self, value=None):
        """Update the key display label"""
        current_key = self.keyboard_key_var.get()
        if hasattr(self, 'key_display'):
            self.key_display.configure(text=current_key)
    
    def save_settings(self):
        """Save current settings to JSON file"""
        try:
            settings = {
                "hours": self.hours_var.get(),
                "minutes": self.minutes_var.get(),
                "seconds": self.seconds_var.get(),
                "milliseconds": self.milliseconds_var.get(),
                "random_offset": self.random_offset_var.get(),
                "random_offset_value": self.random_offset_value_var.get(),
                "mouse_button": self.mouse_button_var.get(),
                "click_type": self.click_type_var.get(),
                "repeat_mode": self.repeat_mode_var.get(),
                "repeat_count": self.repeat_count_var.get(),
                "position_mode": self.position_mode_var.get(),
                "x_pos": self.x_pos_var.get(),
                "y_pos": self.y_pos_var.get(),
                "keyboard_key": self.keyboard_key_var.get(),
                "automation_mode": self.automation_mode_var.get()
            }
            
            with open(self.settings_file, 'w') as f:
                json.dump(settings, f, indent=2)
            
            self.status_label.configure(text="💾 Settings saved successfully!")
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            self.status_label.configure(text="❌ Failed to save settings")
            return False
    
    def load_settings(self):
        """Load settings from JSON file"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    settings = json.load(f)
                
                # Apply loaded settings
                self.hours_var.set(settings.get("hours", "0"))
                self.minutes_var.set(settings.get("minutes", "0"))
                self.seconds_var.set(settings.get("seconds", "0"))
                self.milliseconds_var.set(settings.get("milliseconds", "100"))
                self.random_offset_var.set(settings.get("random_offset", False))
                self.random_offset_value_var.set(settings.get("random_offset_value", "40"))
                self.mouse_button_var.set(settings.get("mouse_button", "Left"))
                self.click_type_var.set(settings.get("click_type", "Single"))
                self.repeat_mode_var.set(settings.get("repeat_mode", "until_stopped"))
                self.repeat_count_var.set(settings.get("repeat_count", "1"))
                self.position_mode_var.set(settings.get("position_mode", "current"))
                self.x_pos_var.set(settings.get("x_pos", "0"))
                self.y_pos_var.set(settings.get("y_pos", "0"))
                self.keyboard_key_var.set(settings.get("keyboard_key", "space"))
                self.automation_mode_var.set(settings.get("automation_mode", "mouse"))
                
                # Update key display if it exists
                if hasattr(self, 'key_display'):
                    self.update_key_display()
                
                print("Settings loaded successfully")
            else:
                print("No settings file found, using defaults")
        except Exception as e:
            print(f"Error loading settings: {e}")
    
    def reset_settings(self):
        """Reset all settings to defaults"""
        self.hours_var.set("0")
        self.minutes_var.set("0")
        self.seconds_var.set("0")
        self.milliseconds_var.set("100")
        self.random_offset_var.set(False)
        self.random_offset_value_var.set("40")
        self.mouse_button_var.set("Left")
        self.click_type_var.set("Single")
        self.repeat_mode_var.set("until_stopped")
        self.repeat_count_var.set("1")
        self.position_mode_var.set("current")
        self.x_pos_var.set("0")
        self.y_pos_var.set("0")
        self.keyboard_key_var.set("space")
        self.automation_mode_var.set("mouse")
        
        if hasattr(self, 'key_display'):
            self.update_key_display()
        
        self.status_label.configure(text="Settings reset to defaults")
    
    def on_closing(self):
        """Handle window closing"""
        self.clicking = False
        self.key_capture_mode = False
        self.position_picking = False
        
        # Auto-save settings on exit
        self.save_settings()
        
        # Stop all listeners
        if self.hotkey_listener:
            try:
                self.hotkey_listener.stop()
            except:
                pass
        if self.key_capture_listener:
            try:
                self.key_capture_listener.stop()
            except:
                pass
        if self.position_listener:
            try:
                self.position_listener.stop()
            except:
                pass
        
        self.root.destroy()

if __name__ == "__main__":
    # Configure pyautogui
    pyautogui.FAILSAFE = True  # Move mouse to corner to stop
    pyautogui.PAUSE = 0.01     # Small pause between actions
    
    app = AutoClicker()
    app.run() 