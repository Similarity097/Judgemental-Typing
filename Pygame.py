import time
def time_thread(self):
	while self.running:
		time.sleep(0.1)
		self.counter += 0.1
		cps = len(self.inpuy_entry())/self.counter
		self.speed_label.config(text=f"speed: \n{cps:.2f} CPS\n{cpm:,2f} CPM)