import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
plt.rcParams['toolbar'] = 'None'

fig = plt.figure()
fig.canvas.set_window_title(' ')
ax1 = fig.add_subplot(2,2,1)

ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

def animate(i):
    pullData1 = open("cpuusage.txt","r").read()
    dataArray1 = pullData1.split('\n')
    xar1 = []
    yar1 = []
    for eachLine in dataArray1:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar1.append(int(x))
            yar1.append(int(y))
    
    pullData2 = open("cputemp.txt","r").read()
    dataArray2 = pullData2.split('\n')
    xar2 = []
    yar2 = []
    for eachLine in dataArray2:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar2.append(int(x))
            yar2.append(int(y))

    pullData3 = open("gpuusage.txt","r").read()
    dataArray3 = pullData3.split('\n')
    xar3 = []
    yar3 = []
    for eachLine in dataArray3:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar3.append(int(x))
            yar3.append(int(y))
    
    pullData4 = open("gputemp.txt","r").read()
    dataArray4 = pullData4.split('\n')
    xar4 = []
    yar4 = []
    for eachLine in dataArray4:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar4.append(int(x))
            yar4.append(int(y))



    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    ax1.plot(xar1,yar1)
    ax2.plot(xar2,yar2)
    ax3.plot(xar3,yar3)
    ax4.plot(xar4,yar4)
    
    ax1.set_ylim([0,100])
    
    ax2.set_ylim([20,60])
    ax3.set_ylim([0,100])
    ax4.set_ylim([30,90])
    
    ax1.set_title("CPU Usage %")
    ax2.set_title("CPU Temp C")
    ax3.set_title("GPU Usage %")
    ax4.set_title("GPU Temp C")
    '''
    ax1.set_ylabel("Percent")
    ax2.set_ylabel("Temp C")
    ax3.set_ylabel("Percent")
    ax4.set_ylabel("Temp C")
    '''
    ax1.set_xticks([])
    ax2.set_xticks([])
    ax3.set_xticks([])
    ax4.set_xticks([])
    
    #plt.xticks(xar1," ")
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()
plt.show()

