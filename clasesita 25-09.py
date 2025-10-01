import numpy as np
import matplotlib.pyplot as plt
import random
#en general se ve bien y da el grafico yo creo que esta bien, no se como sea tu profe pero felipe tambien lo miro y dijo que esta bien

vector_original = np.array([random.uniform(0, 100) for _ in range(720)])

print(f"Vector original (primeros 10 elementos): {vector_original[:10]}\n")

matriz_reshaped = vector_original.reshape(120, 6)
print(f"Matriz con reshape (primeros 3x6 elementos):\n{matriz_reshaped[:3, :]}\n")

matriz_transpuesta = matriz_reshaped.T

copia_f_order = np.array(matriz_transpuesta, order='F')

copia_c_order = np.array(matriz_transpuesta, order='C')

print(f"Matriz Transpuesta (primeros 6x3 elementos):\n{matriz_transpuesta[:, :3]}\n")
print(f"Copia F-order (primeros 6x3 elementos):\n{copia_f_order[:, :3]}\n")
print(f"Copia C-order (primeros 6x3 elementos):\n{copia_c_order[:, :3]}\n")


print(f"¿Son idénticas la transpuesta y copia_f_order?: {np.array_equal(matriz_transpuesta, copia_f_order)}")
print(f"¿Son idénticas la transpuesta y copia_c_order?: {np.array_equal(matriz_transpuesta, copia_c_order)}")
print(f"¿Es la transpuesta C-contiguous?: {matriz_transpuesta.flags['C_CONTIGUOUS']}")
print(f"¿Es copia_f_order F-contiguous?: {copia_f_order.flags['F_CONTIGUOUS']}")
print(f"¿Es copia_c_order C-contiguous?: {copia_c_order.flags['C_CONTIGUOUS']}\n")


fig = plt.figure(figsize=(18, 12)) # a mano

gs = fig.add_gridspec(3, 3, width_ratios=[1, 2, 1], height_ratios=[2, 1, 2])

data_rows = [matriz_reshaped[i, :] for i in range(6)] #  primeras 6 como ejemplo

# Gráfico 1
ax0 = fig.add_subplot(gs[0, 0])
ax0.plot(data_rows[0], 'o-', color='teal', linewidth=2, markersize=8, label='Fila 1 Data')
ax0.set_title('Tendencia de la Fila 1', fontsize=14, color='darkgreen')
ax0.set_xlabel('Índice del Dato', fontsize=12)
ax0.set_ylabel('Valor', fontsize=12)
ax0.grid(True, linestyle='--', alpha=0.7)
ax0.legend(loc='upper left')
ax0.set_facecolor('#f0f8ff') #color suavecito, quedo mas bonito👌

# Gráfico 2
ax1 = fig.add_subplot(gs[0, 1])
x_scatter = np.arange(len(data_rows[1]))
ax1.scatter(x_scatter, data_rows[1], color='crimson', s=100, alpha=0.7, edgecolors='black', label='Fila 2 Puntos')
ax1.set_title('Dispersión de la Fila 2', fontsize=14, color='darkred')
ax1.set_xlabel('Posición', fontsize=12)
ax1.set_ylabel('Magnitud', fontsize=12)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right')
ax1.axhline(np.mean(data_rows[1]), color='gray', linestyle='--', label='Media') # Línea de media
ax1.set_facecolor('#fffafa')

# Gráfico 3
ax2 = fig.add_subplot(gs[0, 2])
bars = ax2.bar(np.arange(len(data_rows[2])), data_rows[2], color=['gold', 'orange', 'darkorange', 'chocolate', 'peru', 'sandybrown'], edgecolor='black', alpha=0.8, label='Fila 3 Valores')
ax2.set_title('Valores de la Fila 3', fontsize=14, color='goldenrod')
ax2.set_xlabel('Categoría', fontsize=12)
ax2.set_ylabel('Altura', fontsize=12)
ax2.grid(axis='y', linestyle='-', alpha=0.4)
ax2.legend(loc='upper right')
ax2.set_facecolor('#ffffe0')

# Gráfico 4 🥲me comí un punto y una coma me tuvo media hora jodiendo, no salia 😒
ax3 = fig.add_subplot(gs[1, 0])
n, bins, patches = ax3.hist(data_rows[3], bins=4, color='darkblue', alpha=0.7, rwidth=0.85, label='Fila 4 Frecuencia')
ax3.set_title('Distribución de Fila 4', fontsize=14, color='midnightblue')
ax3.set_xlabel('Rango de Valor', fontsize=12)
ax3.set_ylabel('Frecuencia', fontsize=12)
ax3.grid(axis='y', linestyle='--', alpha=0.7)
ax3.legend(loc='upper right')
ax3.set_facecolor('#e0ffff')

# Gráfico 5
ax4 = fig.add_subplot(gs[1, 1:]) 
# jajaja debia sumar 100% de razon me daba todo raro😐jajaja si reina no lo note antes cuando me preguntaste es que se me olvidaron algunas cosas no lo he practicado desde el semestre pasado
pie_data = np.abs(data_rows[4]) # mari creo que mejor valor absoluto por si hay negativos salen raros, o no ? si reina te ahorras errores
total = np.sum(pie_data)
if total == 0: # para qe no quede dividieno por cero en el videito estaba (●'◡'●)
    pie_percentages = np.ones(len(pie_data)) / len(pie_data)
else:
    pie_percentages = pie_data / total * 100

wedges, texts, autotexts = ax4.pie(pie_percentages,
                                   labels=[f'Dato {i+1}' for i in range(len(pie_percentages))],
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   explode=[0.05] * len(pie_percentages),
                                   colors=plt.cm.Pastel1.colors, 
                                   pctdistance=0.85)#mari para el parcial me das otra clasesita de esto me enriedo🥺 y se me olvidan cositas 
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
ax4.set_title('Composición de la Fila 5 (Porcentajes)', fontsize=14, color='indigo')
ax4.axis('equal')  
ax4.set_facecolor('#f5f5dc')

# Gráfico 6
ax5 = fig.add_subplot(gs[2, :]) # ocupa las 3 columnas en la fila de abajo
ax5.plot(data_rows[5], label='Fila 6 Original', color='darkgreen', linestyle='-', marker='s', markersize=5, alpha=0.8)
# mari añadi otra línea para comparar tu que dices si queda bien? si reina en general te daba bien antes de todos modos
smoothed_data = np.convolve(data_rows[5], np.ones(3)/3, mode='valid') 
ax5.plot(np.arange(len(smoothed_data)), smoothed_data, label='Fila 6 Suavizada (MV)', color='purple', linestyle='--', marker='o', markersize=4, alpha=0.7)
ax5.set_title('Comparación de Fila 6 (Original vs. Suavizada)', fontsize=14, color='darkmagenta')
ax5.set_xlabel('Punto de Dato', fontsize=12)
ax5.set_ylabel('Valor Suavizado', fontsize=12)
ax5.grid(True, linestyle='-.', alpha=0.6)
ax5.legend(loc='upper right', fontsize=10)
ax5.fill_between(np.arange(len(data_rows[5])), data_rows[5], color='lightgreen', alpha=0.2) #rellenito(●'◡'●)te mando el video donde explicaqn mas cosas para que quede bonito como te gusta
ax5.set_facecolor('#e6e6fa') 


# titulito general de la figura
fig.suptitle('Análisis Multifacético de Datos Numéricos', fontsize=20, fontweight='bold', color='navy', y=1.02)

plt.tight_layout(rect=[0, 0, 1, 0.98]) # espacio para mi supertitulote 😎
plt.show() # se acabooo🥳 mas no le meto 😒o que le falta? no reina tranqui te quedo bien, solo lo del rellenito de resto lo tenias bien 