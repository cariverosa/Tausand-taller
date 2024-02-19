import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import keyboard
import time

class grafica_tiempo_real:                 #Creación de la clase que ejecutará el programa con base en cada una de las funciones
    def __init__(self):
        self.tiempos = []                  #Declaración de variables
        self.valores = []
        self.suma_acumulada = 0
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.ax.set_xlabel('Tiempo (s)')
        self.ax.set_ylabel('Suma acumulada')
        self.tiempo_inicial = time.time()

    def actualizar_grafica(self, frame):
        tiempo_actual = time.time() - self.tiempo_inicial
        self.tiempos.append(tiempo_actual)                #Se van agregando los tiempos a una lista y los valores de la suma a otra lista
        self.valores.append(self.suma_acumulada)

        if tiempo_actual > 30:                            #Condicional para que la gráfica solo muestre los últimos 30 segundos de actividad
            self.tiempos = self.tiempos[-30:]
            self.valores = self.valores[-30:]
            
        #Ubica los registros en la gráfica y autoescala los ejes basado en la actividad de los últimos 30 segundos
        self.line.set_data(self.tiempos, self.valores)   
        self.ax.relim()
        self.ax.autoscale_view()

    def oprimir_teclas(self, e):
        if e.event_type == keyboard.KEY_DOWN:
            if '1' <= e.name <= '5':
                valor = int(e.name)
                self.suma_acumulada += valor
                print(f"Tecla {valor} presionada. Suma acumulada: {self.suma_acumulada}")

            elif e.name == 'r':           # Reinicia el contador                                        
                self.suma_acumulada = 0
                print("Contador reiniciado.")

            elif e.name == 'e':          # Finaliza el programa
                plt.close(self.fig)
                print("Programa finalizado.")
                exit()
            

    def run(self):         #Llama la clase FuncAnimation para que grafique en tiempo real la función actualizar_gráfica actualizandose cada segundo.
        ani = FuncAnimation(self.fig, self.actualizar_grafica, interval=1000)    
        keyboard.hook(self.oprimir_teclas)
        plt.show()


if __name__ == "__main__":
    live_plot = grafica_tiempo_real()
    live_plot.run()
