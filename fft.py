# The script to generate the waves on various frequencies
# and then to analyse their spectrum
import numpy as np
from matplotlib import pyplot as plt
# Uncomment to print the large arrays
import sys
np.set_printoptions(threshold=sys.maxsize)

SAMPLE_RATE = 22050
DURATION = 1

# Generate the x(time) axis
def generate_time_axis():
    x = np.linspace(0, DURATION, SAMPLE_RATE*DURATION, endpoint=False)
    return x

# The sine wave generation
def generate_sine_wave(freq, coordinates):
    frequencies = coordinates * freq
    # Generate the y(amplitude) axis
    y = np.round(np.sin((2 * np.pi) * frequencies), 2)
    return y

# Generate the time axis
x = generate_time_axis()
# Generate the 500 Hz sine wave
y1 = generate_sine_wave(500, x)
# Generate the 750 Hz sine wave
y2 = generate_sine_wave(750, x)
# Generate the 300 Hz sine wave
y3 = generate_sine_wave(300, x)
# Mix the waves
data = y1 + y2 * 0.5 + y3 * 0.3

# Input data size
N = SAMPLE_RATE * DURATION
yf = np.fft.rfft(data)
xf = np.fft.rfftfreq(N, 1 / SAMPLE_RATE)
ryf = np.abs(yf)
# Show plot 
plt.plot(xf, ryf)
plt.show()
