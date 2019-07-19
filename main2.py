import tkinter as tk
from glob import glob
import json
from PIL import Image,ImageTk  

MAIN_PATH = '/home/jude/Documents/artem/dev/NAFAA/'
SOUPLESSE_PIC_PATH = MAIN_PATH + 'Souplesse/'


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.config = json.load(open('config.json','r'))
        
        # Initialize GUI
        self.title("Stretching trainer")
        self.geometry("%sx%s" % (int(self.winfo_screenwidth()/1.9), int(self.winfo_screenheight()/1.9)))
        self.resizable(False, False)
        self._init_mainframe()
            
        
        self.img_list = self.get_image_list()
        
    def get_image_list(self):
        img_list= []
        if self.up_radio_bool.get(): 
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'A*.JPG')
        if self.middle_radio_bool.get(): 
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'B*.JPG')
        if self.down_radio_bool.get(): 
            img_list = img_list + glob(SOUPLESSE_PIC_PATH+'C*.JPG')
        return img_list
    
    def click_part_radio(self):
        self.img_list = self.get_image_list()
        self.config['up'] = self.up_radio_bool.get()
        self.config['mid'] = self.middle_radio_bool.get()
        self.config['bot'] = self.down_radio_bool.get()
        with open('config.json','w') as config_file:
            json.dump(self.config, config_file)
    
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
        self.pictureframe = tk.Frame(self.mainframe, borderwidth=1, padx = 20,pady = 20, relief=tk.GROOVE)
#        self.image = Image.open("/home/jude/Documents/artem/dev/NAFAA/Souplesse/B002.JPG") 
#        photo = ImageTk.PhotoImage(self.image)  
        self.canva = tk.Label(self.pictureframe)#, image=photo)  
        self.canva.pack(side='top', fill='both', expand='yes')  
        
    def _init_timeframe(self):
        self.timeframe = tk.Frame(self.mainframe, borderwidth=1, padx = 20, pady=50,relief=tk.GROOVE)
        led_size = int(self.timeframe.winfo_width())
        self.led_canva = tk.Canvas(self.timeframe, height = led_size, width = led_size)
        self.led_canva.create_oval(5, 5, led_size-5, led_size-5, fill="red", width = 0)
        self.led_canva.pack()
        
        tk.Label(self.timeframe).pack()
        
        tk.Label(self.timeframe, text="Durée :", font = ("Helvetica", 32)).pack(fill = tk.X)
        self.exercice_time_timer = tk.Label(self.timeframe, text=".... / ....", font = ("Helvetica", 28))
        self.exercice_time_timer.pack(fill = tk.X)
  
        tk.Label(self.timeframe).pack()
  
        tk.Label(self.timeframe, text="Durée Totale :", font = ("Helvetica", 20)).pack(fill = tk.X)        
        self.global_time_timer = tk.Label(self.timeframe, text="..:..:../..:..:..", font = ("Helvetica", 15))
        self.global_time_timer.pack(fill = tk.X)
        
    def _init_paramframe(self):
        self.paramframe = tk.LabelFrame(self.configframe, text='Paramètres', font = 15, borderwidth=2, padx = 20, pady = 10,  relief=tk.GROOVE)
        
        tk.Label(self.paramframe, text="Durée de l'exercice", anchor = 'nw', font = 15).pack(fill = tk.X)
        self.timer_scale = tk.Scale(self.paramframe,orient='horizontal', from_=0, to=120, command = print)
        self.timer_scale.pack(fill = tk.X)
        
        tk.Label(self.paramframe).pack()
        
        tk.Label(self.paramframe, text="Durée du repos", anchor = 'nw', font = 15).pack(fill = tk.X)
        self.rest_scale = tk.Scale(self.paramframe,orient='horizontal', from_=0, to=30, command = print)
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
        
        self.start_pause_btn = tk.Button(self.buttonframe, text = 'START', font = 20)
        self.start_pause_btn.pack(fill='both', expand=True)
        
        self.stop_btn = tk.Button(self.buttonframe, text = 'STOP', font = 20, state = "disabled")
        self.stop_btn.pack(fill='both', expand=True)


app().mainloop()


#======================================================