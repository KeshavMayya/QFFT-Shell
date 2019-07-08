from pyquil.api import WavefunctionSimulator

import plotly.plotly as py            #Unimplemented
import matplotlib.pyplot as plt       #Unimplemented


from math import pi
from numpy.fft import ifft


add_dummy_qubits = Program(I(1), I(2))  # The identity gate I has no affect

wf_sim = WavefunctionSimulator()
wavefunction = wf_sim.wavefunction(state_prep + add_dummy_qubits)

#print(wavefunction)


def qft3(q0, q1, q2):
    p = Program()
    p += [SWAP(q0, q2),
          H(q0),
          CPHASE(-pi / 2.0, q0, q1),
          H(q1),
          CPHASE(-pi / 4.0, q0, q2),
          CPHASE(-pi / 2.0, q1, q2),
          H(q2)]
    return p

compute_qft_prog = state_prep + qft3(0, 1, 2)
wavefunction = wf_sim.wavefunction(compute_qft_prog)

#print(wavefunction.amplitudes)

result = ifft(wavefunction.amplitudes, norm="ortho")

print(result)

#Implement pyplot/mpl for plotting.
