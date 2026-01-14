import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import shutil
from pathlib import Path
import subprocess
import threading
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class ValorantOptimizationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Valorant Optimization Tool Pro")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        
        # Set color scheme
        self.bg_color = "#1a1a2e"
        self.accent_color = "#ff4655"
        self.text_color = "#ffffff"
        self.secondary_bg = "#16213e"
        self.success_color = "#00ff88"
        
        self.root.configure(bg=self.bg_color)
        
        # Config path
        self.config_path = Path(os.environ['LOCALAPPDATA']) / "VALORANT" / "Saved" / "Config"
        
        self.create_widgets()
        self.check_config_status()
    
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=15)
        
        title_label = tk.Label(
            title_frame,
            text="VALORANT OPTIMIZATION TOOL",
            font=("Arial", 22, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Fix Lag, Stuttering & Boost Performance",
            font=("Arial", 11),
            fg=self.text_color,
            bg=self.bg_color
        )
        subtitle_label.pack()
        
        # Status Frame
        status_frame = tk.Frame(self.root, bg=self.secondary_bg, relief=tk.RIDGE, bd=2)
        status_frame.pack(pady=8, padx=20, fill=tk.X)
        
        tk.Label(
            status_frame,
            text="Config Status:",
            font=("Arial", 10, "bold"),
            fg=self.text_color,
            bg=self.secondary_bg
        ).pack(anchor=tk.W, padx=10, pady=3)
        
        self.status_label = tk.Label(
            status_frame,
            text="Checking...",
            font=("Arial", 9),
            fg=self.success_color,
            bg=self.secondary_bg
        )
        self.status_label.pack(anchor=tk.W, padx=10, pady=3)
        
        # Create Notebook (Tabs)
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Style for notebook
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background=self.bg_color, borderwidth=0)
        style.configure('TNotebook.Tab', background=self.secondary_bg, foreground=self.text_color, 
                       padding=[20, 10], font=('Arial', 10, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', self.accent_color)], 
                 foreground=[('selected', self.text_color)])
        
        # Tab 1: Valorant Fixes
        valorant_frame = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(valorant_frame, text="🎮 Valorant Fixes")
        
        self.create_valorant_tab(valorant_frame)
        
        # Tab 2: System Optimization
        system_frame = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(system_frame, text="⚡ System Optimization")
        
        self.create_system_tab(system_frame)
        
        # Tab 3: Quick Actions
        quick_frame = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(quick_frame, text="🚀 Quick Actions")
        
        self.create_quick_tab(quick_frame)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="Made with ❤️ for smooth gameplay | Share with friends!",
            font=("Arial", 8),
            fg="#888888",
            bg=self.bg_color
        )
        footer_label.pack(side=tk.BOTTOM, pady=8)
    
    def create_valorant_tab(self, parent):
        # Reset Config Button
        self.reset_btn = tk.Button(
            parent,
            text="🔄 RESET CONFIG FILES",
            font=("Arial", 11, "bold"),
            bg=self.accent_color,
            fg=self.text_color,
            activebackground="#cc3844",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.reset_config,
            height=2
        )
        self.reset_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Clear Shader Cache Button
        shader_btn = tk.Button(
            parent,
            text="🗑️ Clear Shader Cache",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_shader_cache
        )
        shader_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Open Config Folder Button
        open_folder_btn = tk.Button(
            parent,
            text="📁 Open Config Folder",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.open_config_folder
        )
        open_folder_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Launch Riot Client Button
        launch_btn = tk.Button(
            parent,
            text="🎮 Launch Riot Client",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.launch_valorant
        )
        launch_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Info
        info_frame = tk.Frame(parent, bg=self.secondary_bg, relief=tk.RIDGE, bd=2)
        info_frame.pack(pady=10, padx=10, fill=tk.X)
        
        info_text = """ℹ️ Valorant Fixes:
• Reset corrupted config files
• Clear shader cache for better FPS
• Quick access to config folder"""
        
        tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 9),
            fg=self.text_color,
            bg=self.secondary_bg,
            justify=tk.LEFT
        ).pack(padx=10, pady=10)
    
    def create_system_tab(self, parent):
        # Flush DNS Button
        dns_btn = tk.Button(
            parent,
            text="🌐 Flush DNS Cache",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.flush_dns
        )
        dns_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Clear Temp Files Button
        temp_btn = tk.Button(
            parent,
            text="🗑️ Clear Temp Files",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_temp_files
        )
        temp_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Clear Windows Cache Button
        cache_btn = tk.Button(
            parent,
            text="💾 Clear Windows Cache",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_windows_cache
        )
        cache_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Clear DirectX Shader Cache Button
        dx_cache_btn = tk.Button(
            parent,
            text="🎨 Clear DirectX Shader Cache",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_directx_cache
        )
        dx_cache_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Clear Prefetch Button
        prefetch_btn = tk.Button(
            parent,
            text="⚡ Clear Prefetch Files",
            font=("Arial", 10),
            bg=self.secondary_bg,
            fg=self.text_color,
            activebackground="#1e2a47",
            activeforeground=self.text_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_prefetch
        )
        prefetch_btn.pack(fill=tk.X, pady=5, padx=10)
        
        # Info
        info_frame = tk.Frame(parent, bg=self.secondary_bg, relief=tk.RIDGE, bd=2)
        info_frame.pack(pady=10, padx=10, fill=tk.X)
        
        info_text = """ℹ️ System Optimizations:
• Flush DNS for better connection
• Clear temp files to free space
• Remove cached data for performance"""
        
        tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 9),
            fg=self.text_color,
            bg=self.secondary_bg,
            justify=tk.LEFT
        ).pack(padx=10, pady=10)
    
    def create_quick_tab(self, parent):
        # One-Click Optimize Button
        optimize_btn = tk.Button(
            parent,
            text="⚡ ONE-CLICK OPTIMIZE ALL",
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg="#000000",
            activebackground="#00cc66",
            activeforeground="#000000",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.optimize_all,
            height=2
        )
        optimize_btn.pack(fill=tk.X, pady=10, padx=10)
        
        # Info
        info_frame = tk.Frame(parent, bg=self.secondary_bg, relief=tk.RIDGE, bd=2)
        info_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(
            info_frame,
            text="🚀 One-Click Optimize Will:",
            font=("Arial", 11, "bold"),
            fg=self.text_color,
            bg=self.secondary_bg
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        optimizations = [
            "✓ Reset Valorant config files",
            "✓ Clear Valorant shader cache",
            "✓ Flush DNS cache",
            "✓ Clear temp files",
            "✓ Clear Windows cache",
            "✓ Clear DirectX shader cache",
            "✓ Clear prefetch files"
        ]
        
        for opt in optimizations:
            tk.Label(
                info_frame,
                text=opt,
                font=("Arial", 9),
                fg=self.success_color,
                bg=self.secondary_bg,
                anchor=tk.W
            ).pack(anchor=tk.W, padx=20, pady=2)
        
        tk.Label(
            info_frame,
            text="\n⚠️ Note: Some operations require admin rights",
            font=("Arial", 9, "italic"),
            fg="#ffaa00",
            bg=self.secondary_bg
        ).pack(padx=10, pady=5)
    
    def check_config_status(self):
        if self.config_path.exists():
            files_count = len(list(self.config_path.rglob("*")))
            self.status_label.config(
                text=f"✓ Config found ({files_count} files)",
                fg=self.success_color
            )
        else:
            self.status_label.config(
                text="✗ Config folder not found",
                fg=self.accent_color
            )
    
    def reset_config(self):
        if not self.config_path.exists():
            messagebox.showerror(
                "Error",
                "Valorant config folder not found!\n\nMake sure Valorant is installed."
            )
            return
        
        result = messagebox.askyesno(
            "Confirm Reset",
            "This will delete all config files.\n\n"
            "You'll need to re-adjust your video settings.\n\n"
            "Continue?"
        )
        
        if result:
            try:
                for item in self.config_path.iterdir():
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                
                messagebox.showinfo(
                    "Success",
                    "✓ Config reset successfully!\n\n"
                    "Launch Valorant and adjust your settings."
                )
                self.check_config_status()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to reset config:\n{str(e)}")
    
    def open_config_folder(self):
        if self.config_path.exists():
            os.startfile(self.config_path)
        else:
            messagebox.showerror("Error", "Config folder not found!")
    
    def clear_shader_cache(self):
        shader_paths = [
            Path(os.environ['LOCALAPPDATA']) / "VALORANT" / "Saved" / "ShaderCache",
            Path(os.environ['LOCALAPPDATA']) / "Riot Games" / "VALORANT" / "Saved" / "ShaderCache"
        ]
        
        cleared = False
        for shader_path in shader_paths:
            if shader_path.exists():
                try:
                    shutil.rmtree(shader_path)
                    shader_path.mkdir(parents=True, exist_ok=True)
                    cleared = True
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to clear shader cache:\n{str(e)}")
                    return
        
        if cleared:
            messagebox.showinfo("Success", "✓ Shader cache cleared!")
        else:
            messagebox.showinfo("Info", "No shader cache found to clear.")
    
    def launch_valorant(self):
        try:
            riot_client_path = Path(os.environ['PROGRAMFILES']) / "Riot Games" / "Riot Client" / "RiotClientServices.exe"
            
            if riot_client_path.exists():
                subprocess.Popen([str(riot_client_path), "--launch-product=valorant", "--launch-patchline=live"])
                messagebox.showinfo("Launching", "Valorant is launching...")
            else:
                subprocess.Popen(["explorer", "riotclient://"])
                messagebox.showinfo("Info", "Opening Riot Client...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Valorant:\n{str(e)}")
    
    def flush_dns(self):
        try:
            subprocess.run(["ipconfig", "/flushdns"], capture_output=True, check=True)
            messagebox.showinfo("Success", "✓ DNS cache flushed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to flush DNS:\n{str(e)}\n\nTry running as administrator.")
    
    def clear_temp_files(self):
        try:
            temp_paths = [
                Path(os.environ['TEMP']),
                Path(os.environ['TMP']),
                Path(os.environ['WINDIR']) / "Temp"
            ]
            
            deleted_count = 0
            for temp_path in temp_paths:
                if temp_path.exists():
                    for item in temp_path.iterdir():
                        try:
                            if item.is_file():
                                item.unlink()
                                deleted_count += 1
                            elif item.is_dir():
                                shutil.rmtree(item)
                                deleted_count += 1
                        except:
                            pass
            
            messagebox.showinfo("Success", f"✓ Cleared {deleted_count} temp files/folders!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear temp files:\n{str(e)}")
    
    def clear_windows_cache(self):
        try:
            cache_paths = [
                Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "Explorer",
                Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "INetCache",
                Path(os.environ['LOCALAPPDATA']) / "Temp"
            ]
            
            deleted_count = 0
            for cache_path in cache_paths:
                if cache_path.exists():
                    for item in cache_path.iterdir():
                        try:
                            if item.is_file():
                                item.unlink()
                                deleted_count += 1
                            elif item.is_dir():
                                shutil.rmtree(item)
                                deleted_count += 1
                        except:
                            pass
            
            messagebox.showinfo("Success", f"✓ Cleared Windows cache ({deleted_count} items)!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear cache:\n{str(e)}")
    
    def clear_directx_cache(self):
        try:
            dx_cache_path = Path(os.environ['LOCALAPPDATA']) / "D3DSCache"
            
            if dx_cache_path.exists():
                deleted_count = 0
                for item in dx_cache_path.iterdir():
                    try:
                        if item.is_file():
                            item.unlink()
                            deleted_count += 1
                    except:
                        pass
                messagebox.showinfo("Success", f"✓ Cleared DirectX shader cache ({deleted_count} files)!")
            else:
                messagebox.showinfo("Info", "DirectX cache folder not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear DirectX cache:\n{str(e)}")
    
    def clear_prefetch(self):
        try:
            prefetch_path = Path(os.environ['WINDIR']) / "Prefetch"
            
            if prefetch_path.exists():
                deleted_count = 0
                for item in prefetch_path.iterdir():
                    try:
                        if item.is_file():
                            item.unlink()
                            deleted_count += 1
                    except:
                        pass
                messagebox.showinfo("Success", f"✓ Cleared {deleted_count} prefetch files!")
            else:
                messagebox.showinfo("Info", "Prefetch folder not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear prefetch:\n{str(e)}\n\nTry running as administrator.")
    
    def optimize_all(self):
        result = messagebox.askyesno(
            "Confirm Optimization",
            "This will perform ALL optimizations:\n\n"
            "• Reset Valorant config\n"
            "• Clear all caches\n"
            "• Flush DNS\n"
            "• Clear temp files\n\n"
            "Continue?"
        )
        
        if result:
            progress_window = tk.Toplevel(self.root)
            progress_window.title("Optimizing...")
            progress_window.geometry("400x200")
            progress_window.configure(bg=self.bg_color)
            progress_window.resizable(False, False)
            
            tk.Label(
                progress_window,
                text="⚡ Optimizing Your System...",
                font=("Arial", 14, "bold"),
                fg=self.accent_color,
                bg=self.bg_color
            ).pack(pady=20)
            
            status_label = tk.Label(
                progress_window,
                text="Starting...",
                font=("Arial", 10),
                fg=self.text_color,
                bg=self.bg_color
            )
            status_label.pack(pady=10)
            
            def run_optimizations():
                operations = [
                    ("Resetting Valorant config...", self.reset_config_silent),
                    ("Clearing shader cache...", self.clear_shader_cache_silent),
                    ("Flushing DNS...", self.flush_dns_silent),
                    ("Clearing temp files...", self.clear_temp_files_silent),
                    ("Clearing Windows cache...", self.clear_windows_cache_silent),
                    ("Clearing DirectX cache...", self.clear_directx_cache_silent),
                    ("Clearing prefetch...", self.clear_prefetch_silent)
                ]
                
                for i, (msg, func) in enumerate(operations):
                    status_label.config(text=msg)
                    try:
                        func()
                    except:
                        pass
                
                progress_window.destroy()
                messagebox.showinfo(
                    "Complete!",
                    "✓ All optimizations completed!\n\n"
                    "Launch Valorant and enjoy smoother gameplay!"
                )
                self.check_config_status()
            
            threading.Thread(target=run_optimizations, daemon=True).start()
    
    # Silent versions (no popups)
    def reset_config_silent(self):
        if self.config_path.exists():
            for item in self.config_path.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                except:
                    pass
    
    def clear_shader_cache_silent(self):
        shader_paths = [
            Path(os.environ['LOCALAPPDATA']) / "VALORANT" / "Saved" / "ShaderCache",
            Path(os.environ['LOCALAPPDATA']) / "Riot Games" / "VALORANT" / "Saved" / "ShaderCache"
        ]
        for shader_path in shader_paths:
            if shader_path.exists():
                try:
                    shutil.rmtree(shader_path)
                    shader_path.mkdir(parents=True, exist_ok=True)
                except:
                    pass
    
    def flush_dns_silent(self):
        try:
            subprocess.run(["ipconfig", "/flushdns"], capture_output=True)
        except:
            pass
    
    def clear_temp_files_silent(self):
        temp_paths = [Path(os.environ['TEMP']), Path(os.environ['TMP'])]
        for temp_path in temp_paths:
            if temp_path.exists():
                for item in temp_path.iterdir():
                    try:
                        if item.is_file():
                            item.unlink()
                        elif item.is_dir():
                            shutil.rmtree(item)
                    except:
                        pass
    
    def clear_windows_cache_silent(self):
        cache_paths = [
            Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "Explorer",
            Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "INetCache"
        ]
        for cache_path in cache_paths:
            if cache_path.exists():
                for item in cache_path.iterdir():
                    try:
                        if item.is_file():
                            item.unlink()
                        elif item.is_dir():
                            shutil.rmtree(item)
                    except:
                        pass
    
    def clear_directx_cache_silent(self):
        dx_cache_path = Path(os.environ['LOCALAPPDATA']) / "D3DSCache"
        if dx_cache_path.exists():
            for item in dx_cache_path.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                except:
                    pass
    
    def clear_prefetch_silent(self):
        prefetch_path = Path(os.environ['WINDIR']) / "Prefetch"
        if prefetch_path.exists():
            for item in prefetch_path.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                except:
                    pass

def main():
    root = tk.Tk()
    app = ValorantOptimizationTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
