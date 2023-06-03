import ltspice
import numpy as np
import matplotlib.pyplot as plt

# Load the signals from the .raw file
raw_file = '../carga_descarga/carga_descarga.raw'
l = ltspice.Ltspice(raw_file)
# Make sure that the .raw file is located in the correct path
l.parse() 

#Obtain basic signals
time = l.get_time()
time = (time - 1E-3)*1E+6   #Convert to useg
Vl = l.get_data('V(vl)')
Vc = l.get_data('V(vc)')

#Obtain currents
il = l.get_data('I(L1)')
ic = l.get_data('I(C1)')

signals = [Vl, il, Vc, ic]
num_signals = len(signals)
labels = ["$V_L$", "$i_L$", "$V_C$", "$i_C$"]

#Set max and min Voltages and currents
V_upper_limit = 13
V_lower_limit = -13
I_upper_limit = 1.5
I_lower_limit = -0.5

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
#Adjust spacing
fig.subplots_adjust(hspace=0.5)
for i, ax in enumerate(axs.flatten()):
    xticks_list = []
    xticks_labels = []
    yticks_list = []
    yticks_labels = []

    if i%2 == 0:    #Voltage signals are odd (0, 2, 4)
        ax.plot(time, signals[i], color = 'red')
        ax.set_title(labels[i] + " $ [V]$")

        ax.plot(time, signals[i], color = 'red')
        
    else:
        ax.set_title(labels[i] + " $[A]$")
        ax.set_ylim(I_lower_limit, I_upper_limit)

        ax.plot(time, signals[i], color = 'blue')

    if labels[i] == "$i_L$":
        ax.plot(time, io, color = 'teal', linestyle='--')
        ax.annotate("$i_o$", xy=(0, io.mean()), xytext=(-1.2, io.mean()),
            arrowprops=dict(facecolor='black', arrowstyle='->'))

    ax.set_xlabel("$Time\ [\mu seg]$")
    ax.grid(False)
    #Set the part we want to see
    #ax.set_xlim(0, N_periods*Ts*1E6)
    
    #Draw vertical lines at the points of switching
    # for i in range(int(N_periods)):
    #     ax.axvline(x=(D*Ts + i*Ts)*1E6, linestyle='--', linewidth = 0.5,color='grey')
    #     ax.axvline(x=(1 + i)*Ts*1E6, linestyle='--', linewidth = 0.5,color='grey')    

    #     xticks_list.append((D*Ts + i*Ts)*1E6)
    #     xticks_list.append((1 + i)*Ts*1E6)

    #     if i == 0:
    #         xticks_labels.append("$DTs$")
    #         xticks_labels.append("$Ts$")
    #     else:
    #         xticks_labels.append("$(D" + "+" + str(i) + ")Ts$")
    #         xticks_labels.append("$" + str(i+1) + "Ts$")

    #     #Agrego el 0
    #     ax.axhline(y= 0, linestyle='--', linewidth = 0.5, color='grey')
    #     yticks_list.append(0)
    #     yticks_labels.append("$0$")

    ax.set_xticks(xticks_list)
    ax.set_yticks(yticks_list)
    ax.set_xticklabels(xticks_labels)
    ax.set_yticklabels(yticks_labels)
#plt.axis([0, 2*np.pi, -1 , 1]) # [xmin, xmax, ymin, ymax]
    ax.yaxis.set_label_coords(-0.01, 0.9)

    
    
#axs[-1, -1].axis('off')  # Hide last subplot if there are an odd number of signals

# Add a legend
#ig.legend([f'Signal {i+1}' for i in range(num_signals)])

# Save the figure to a PDF file
plt.savefig('Buck_CCM_signals.pdf')