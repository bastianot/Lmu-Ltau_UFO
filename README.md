# Lmu-Ltau_UFO

This repository includes an UFO file for the gauged U(1)Lmu-Ltau-Model which includes the SM, a new Z', a singlet scalar and three right-handed neutrinos. We provide additionally a set of valid parameter points which generate the neutrino oscillations of SM neutrinos at 2sigma while evading cosmological constraints. A python script is included to generate the according mixing matrices.

# Instructions

The folder 'L_mu-L_tau' is the UFO model file and should be placed in the model-folder of MadGraph 5 (we have tested MG5 version 3.4.2).

If one wants to change the parameters of the model, it is recommended to do this in the first few lines of the file 'writeParameters.py'. The parameters 'M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau' are Majorana and Dirac masses of the RH (and LH) neutrinos. They should be chosen to agree with neutrino oscillations. Therefore, two datasets of a sample of allowed values are given for the general case ('generalPoints100.csv' and 'generalPoints15.csv' where the number denotes the mass of the Z' in MeV) and the UV complete theory ('uvPoints100.csv' and 'uvPoints15.csv', valid up to 10^16 GeV according to one-loop RG equations). We provide the corresponding heavy neutrino masses such that a choice can be made reasonably.

The other parameters are explained in the following (one has to choose these in agreement with experiments):   
	'MZp':mass of the Z' [GeV]  
	'gmutau': new gauge coupling  
	'MH2': mass of the Lmu-Ltau charged Higgs boson [GeV]  
	'Sa': sine of the mixing angle alpha between the SM Higgs and the new Higgs.  

Then the script may be run via 'python3 writeParameters.py'. An output is generated in the console which shows the according neutrino oscillation parameters. Also, the parameters are given in appropriate format in 'parametersPy.txt'to be pasted into the UFO file 'parameters.py'. Note that one should change only the lines ~27-638 of 'parameters.py'(between the comment blocks) by completely overwriting these lines with the whole text of 'parametersPy.txt'.
