#!/usr/bin/python3
import tkinter as tk
from glob import glob
import json
from PIL import Image, ImageTk

import threading
import time

MAIN_PATH = '/home/jude/Documents/artem/dev/NAFAA/'
SOUPLESSE_PIC_PATH = MAIN_PATH + 'Souplesse/'
RATIO = 1.9

class app(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config = json.load(open('config.json','r'))
        self.streching_time = int(self.config['timer'])
        self.rest_time = int(self.config['rest'])

        self._init_var()
        
        # Initialize GUI
        self.title("Stretching trainer")
        #self.geometry("%sx%s" % (int(self.winfo_screenwidth()/RATIO), int(self.winfo_screenheight()/RATIO)))
        self.geometry('1010x568')
        self.resizable(False, False)
        self._init_mainframe()

        self.img_list = self.get_image_list()
        self.define_global_time()

    def runner(self):
        if self.isrunning:
            if self.isrest and int(self.curr_timer) == int(self.rest_time):
                self.isrest = False
                self.curr_timer = 0
            elif not self.isrest and int(self.curr_timer) == int(self.streching_time):
                self.isrest = True
                self.curr_timer = 0
                if len(self.img_list) - 1 == self.pic_index:
                    self.click_stop_button()
                else:
                    self.pic_index += 1
                
            if self.isrest:
                self.get_picture()
                self.define_global_time()
                self.define_strech_time(self.rest_time)
                self.draw_led('red')
            else:
                self.get_picture()
                self.define_global_time()
                self.define_strech_time(self.streching_time)
                self.draw_led('green')    
            
            if not self.ispause:
                self.curr_timer += 1
                self.full_timer += 1
            
            time.sleep(1)
            self.runner()

    def click_next_button(self):
        self.isrest = True
        self.curr_timer = 0
        if len(self.img_list) - 1 == self.pic_index:
            self.click_stop_button()
        else:
            self.pic_index += 1
            
    def _init_var(self):
        self.curr_timer = 0
        self.full_timer = 0
        self.pic_index = 0
        
        self.isrunning = False
        self.ispause = False
        self.isrest = True
        
    def lets_start(self):
        self.stop_btn.config(state='normal')
        self.next_btn.config(state='normal')
        self.timer_scale.config(state='disabled')
        self.rest_scale.config(state='disabled')
        self.up_radio.config(state='disabled')
        self.middle_radio.config(state='disabled')
        self.bot_radio.config(state='disabled')
        self.isrunning = True
        
    def get_picture(self):
        self.picture = self.img_list[self.pic_index]
        im=Image.open(self.picture)
        self.photo=ImageTk.PhotoImage(im)
        self.img_canva.create_image(0, 0, image=self.photo, anchor = 'nw')

    def click_start_button(self):
        if not self.isrunning: 
            self.lets_start()
            self.run = threading.Thread(target = self.runner, name = 'runner').start()
        else: self.ispause = not self.ispause
        if self.ispause: 
            self.start_pause_btn.config(text = 'PAUSE')
        else:
            self.start_pause_btn.config(text = 'CONTINUE')
        
    def click_stop_button(self):
        self.isrunning = False
        self.ispause = False
        self.stop_btn.config(state='disabled')
        self.next_btn.config(state='disabled')
        
        self.timer_scale.config(state='normal')
        self.rest_scale.config(state='normal')
        self.up_radio.config(state='normal')
        self.middle_radio.config(state='normal')
        self.bot_radio.config(state='normal')
        self.start_pause_btn.config(text = 'START')
        self.img_canva.delete("all")
        self._init_var()
    
    def get_image_list(self):
        img_list= []
        if self.up_radio_bool.get():
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'A*.JPG')
        if self.middle_radio_bool.get():
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'B*.JPG')
        if self.down_radio_bool.get():
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'C*.JPG')
        return sorted(img_list)

    def click_part_radio(self):
        self.img_list = self.get_image_list()
        self.config['up'] = self.up_radio_bool.get()
        self.config['mid'] = self.middle_radio_bool.get()
        self.config['bot'] = self.down_radio_bool.get()
        with open('config.json','w') as config_file:
            json.dump(self.config, config_file)
        self.define_global_time()

    def click_slide_time(self, value):
        self.streching_time = value
        self.config['timer'] = self.streching_time
        with open('config.json','w') as config_file:
            json.dump(self.config, config_file)
        self.define_global_time()

    def click_slide_rest(self, value):
        self.rest_time = value
        self.config['rest'] = self.rest_time
        with open('config.json','w') as config_file:
            json.dump(self.config, config_file)
        self.define_global_time()

    def get_strech_timer(self, ref):
        return str("%02d / %02d" % (int(self.curr_timer), int(ref)))

    def define_strech_time(self, ref):
        self.exercice_time_timer['text'] = self.get_strech_timer(ref)

    def compute_global_time(self):
        pic_nb = len(self.img_list)
        time = int(self.streching_time) * int(pic_nb) + int(self.rest_time) * (int(pic_nb))
        return time

    def get_global_time(self):
        ref = self.compute_global_time()
        ex_min = self.full_timer //60
        ex_sec = self.full_timer % 60
        ref_min = ref//60
        ref_sec = ref%60
        return str("%02d:%02d / %02d:%02d" % (int(ex_min), int(ex_sec), int(ref_min), int(ref_sec)))

    def define_global_time(self):
        self.global_time_timer['text'] = self.get_global_time()

    def _init_mainframe(self):
        self.mainframe = tk.Frame(self, bg='white')
        self.mainframe.pack(fill='both', expand=True)
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=5)
        self.mainframe.grid_columnconfigure(2, weight=2)

        self._init_configframe()
        self.configframe.grid(row=0, column = 0, sticky = "nswe")

        self._init_pictureframe()
        self.pictureframe.grid(row=0, column = 1, sticky = "nswe")

        self._init_timeframe()
        self.timeframe.grid(row=0, column = 2, sticky = "nswe")

    def _init_configframe(self):
        self.configframe = tk.Frame(self.mainframe, borderwidth=1, padx = 20, pady = 20, relief=tk.GROOVE )

        self._init_paramframe()
        self.paramframe.pack(fill='both', expand=True)

        tk.Label(self.configframe).pack()

        self._init_partframe()
        self.partframe.pack(fill='both', expand=True)
        tk.Label(self.configframe).pack()

        self._init_buttonframe()
        self.buttonframe.pack(fill='both', expand=True)

    def _init_pictureframe(self):
        self.pictureframe = tk.Frame(self.mainframe, borderwidth=0)
        self.img_canva = tk.Canvas(self.pictureframe, bg='white', width = 456, height = 567)
        self.img_canva.pack()
    
    def draw_led(self, color):
        led_size = int(self.winfo_screenwidth()*0.05)
        self.led_canva.create_oval(5, 5, led_size-5, led_size-5, fill=color, width = 0)
        
    def _init_timeframe(self):
        self.timeframe = tk.Frame(self.mainframe, borderwidth=1, padx = 20, pady=50,relief=tk.GROOVE)
        led_size = int(self.winfo_screenwidth()*0.05)
        self.led_canva = tk.Canvas(self.timeframe, height = led_size, width = led_size)
        self.led_canva.pack()
        self.draw_led('red')
        tk.Label(self.timeframe).pack()

        tk.Label(self.timeframe, text="Durée :", font = ("Helvetica", 32)).pack(fill = tk.X)
        self.exercice_time_timer = tk.Label(self.timeframe, text="... / ...", font = ("Helvetica", 28))
        self.exercice_time_timer.pack(fill = tk.X)

        tk.Label(self.timeframe).pack()

        tk.Label(self.timeframe, text="Durée Totale :", font = ("Helvetica", 20)).pack(fill = tk.X)
        self.global_time_timer = tk.Label(self.timeframe, text="..:..:.. / ..:..:..", font = ("Helvetica", 15))
        self.global_time_timer.pack(fill = tk.X)

    def _init_paramframe(self):
        self.paramframe = tk.LabelFrame(self.configframe, text='Paramètres', font = 15, borderwidth=2, padx = 20, pady = 10,  relief=tk.GROOVE)

        tk.Label(self.paramframe, text="Durée de l'exercice", anchor = 'nw', font = 15).pack(fill = tk.X)
        self.timer_scale = tk.Scale(self.paramframe,orient='horizontal', from_=0, to=120, command = self.click_slide_time)
        self.timer_scale.set(self.streching_time)
        self.timer_scale.pack(fill = tk.X)

        tk.Label(self.paramframe).pack()

        tk.Label(self.paramframe, text="Durée du repos", anchor = 'nw', font = 15).pack(fill = tk.X)
        self.rest_scale = tk.Scale(self.paramframe,orient='horizontal', from_=0, to=30, command = self.click_slide_rest)
        self.rest_scale.set(self.rest_time)
        self.rest_scale.pack(fill = tk.X)

    def _init_partframe(self):
        self.partframe = tk.LabelFrame(self.configframe, text='Partie du corps', font = 15, borderwidth=2, padx = 20, pady = 10, relief=tk.GROOVE)
        self.up_radio_bool = tk.BooleanVar()
        self.up_radio_bool.set(self.config['up'])
        self.middle_radio_bool = tk.BooleanVar()
        self.middle_radio_bool.set(self.config['mid'])
        self.down_radio_bool = tk.BooleanVar()
        self.down_radio_bool.set(self.config['bot'])

        self.up_radio = tk.Checkbutton(self.partframe, text='Haut', var = self.up_radio_bool, anchor = 'nw', font = 15, command = self.click_part_radio)
        self.up_radio.pack(fill = tk.X)

        self.middle_radio = tk.Checkbutton(self.partframe, text='Milieu', var = self.middle_radio_bool, anchor = 'nw', font = 15, command = self.click_part_radio)
        self.middle_radio.pack(fill = tk.X)

        self.bot_radio = tk.Checkbutton(self.partframe, text='Bas', var = self.down_radio_bool, anchor = 'nw', font = 15, command = self.click_part_radio)
        self.bot_radio.pack(fill = tk.X)

    def _init_buttonframe(self):
        self.buttonframe = tk.Frame(self.configframe, borderwidth=0, padx = 20, pady = 10)

        self.start_pause_btn = tk.Button(self.buttonframe, text = 'START', font = 20, command = self.click_start_button)
        self.start_pause_btn.pack(fill='both', expand=True)
        
        self.next_btn = tk.Button(self.buttonframe, text = 'NEXT', font = 20, state = "disabled", command = self.click_next_button)
        self.next_btn.pack(fill='both', expand=True)

        self.stop_btn = tk.Button(self.buttonframe, text = 'STOP', font = 20, state = "disabled", command = self.click_stop_button)
        self.stop_btn.pack(fill='both', expand=True)

if __name__ == '__main__':
    app().mainloop()
