import numpy as np

nori = 'normal'#'normal' or 'inverted'
##########################
#Change parameters here
##########################
MZp = 0.1
gmutau = 0.0009
MH2 = 50
Sa = 0.006
M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau = 192.815693112102,	127.605763088904,	186.368669337741,	157.289275454027,	3.1830634288236,	0.000108652304494,	9.00302204177961E-05,	0.000107707912415



##########################
def WCalc(M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau):
    
    M_R = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    M_RDag = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    h = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    hr = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    M_R[0,0]=M_ee
    M_R[0,1]=V_emu
    M_R[0,2]=V_etau
    M_R[1,0]=V_emu
    M_R[1,1]=0
    M_R[1,2]=M_mutau*np.exp(complex(0,Xi))
    M_R[2,0]=V_etau
    M_R[2,1]=M_mutau*np.exp(complex(0,Xi))
    M_R[2,2]=0
    
    M_D = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    M_D[0,0]=f_e
    M_D[1,1]=f_mu
    M_D[2,2]=f_tau
    
    
    M_RDag = np.transpose(M_R)
    M_RDag = np.conjugate(M_RDag)
    
    hr = M_R @ M_RDag
    
    lamH, V = np.linalg.eigh(hr)
    lamH[:] = np.abs(lamH[:])
    mH = np.zeros(3)
    mH = np.sqrt(lamH[:])
    mH = np.sort(mH[:])

    M_nu = -M_D @ (np.linalg.inv(M_R)@M_D)
    M_nuDag = np.transpose(M_nu)
    M_nuDag = np.conjugate(M_nuDag)
    
    h = M_nu @ M_nuDag
    
    lam, U2 = np.linalg.eigh(h)
    lam[:] = np.abs(lam[:])
    
    
    
    
    if np.imag(lam[0])>= 0.00001 or np.imag(lam[2])>= 0.00001 or np.imag(lam[2])>= 0.00001:
        print("error:lambda complex")
    
      
    lam = np.array([np.real(lam[0]),np.real(lam[1]),np.real(lam[2])])
    # generate normal or inverted mass ordering
    
    if lam[0]>0 and lam[1]>0 and lam[2]>0: #ensure physical masses
        
        m = np.zeros(3)
        m = np.sqrt(lam[:])
        
        m = np.sort(m[:])
        
        
        if nori == 'normal':
            pass
        elif nori == 'inverted':
            mcopy = np.zeros(3)
            mcopy[:]= m[:]
            m[1] = mcopy[2]
            m[0] = mcopy[1]
            m[2] = mcopy[0]
        else:
            print('normal or inverted?')
            
        
        
        
        #calculate unitary matrix U

          

        absN = np.zeros(3)

        for i in range(3):

            absN[i] = np.real(np.sqrt(np.abs((h[1,1]-m[i]**2)*h[0,2]-h[0,1]*h[1,2])**2+\
                            np.abs((h[0,0]-m[i]**2)*h[1,2]-np.conjugate(h[0,1])*h[0,2])**2+\
                            (np.abs(h[0,1])**2-(h[0,0]-m[i]**2)*(h[1,1]-m[i]**2))**2))

        U = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
        
        for i in range(3):
            U[0,i] = ((h[1,1]-m[i]**2)*h[0,2]-h[0,1]*h[1,2])/absN[i]
            U[1,i] = ((h[0,0]-m[i]**2)*h[1,2]-np.conjugate(h[0,1])*h[0,2])/absN[i]
            U[2,i] = (np.abs(h[0,1])**2-(h[0,0]-m[i]**2)*(h[1,1]-m[i]**2))/absN[i]
        
        #you could obtain the light neutrino parameters here
        #calculate mixing angles
        
        Theta_23 = np.arctan(np.abs(U[1,2])/np.abs(U[2,2]))
        Theta_12 = np.arctan(np.abs(U[0,1])/np.abs(U[0,0]))
        Theta_13 = np.arcsin(np.abs(U[0,2]))
        
        #calculate Dirac CP phase
        if Theta_23 != 0.0 and Theta_23 != np.pi/2 and Theta_23 != np.pi and Theta_12 != 0.0 and Theta_12 != np.pi/2\
                and Theta_12 != np.pi and Theta_13 != np.pi/2 and Theta_13 != 3*np.pi/2 and Theta_13 != 0.0 \
                and Theta_13 != np.pi and m[1]**2-m[0]**2!=0.0 and m[2]**2-m[1]**2 !=0.0 and m[2]**2-m[0]**2!=0.0 :
            
            alpha = (8*np.imag(h[0,1]*h[1,2]*h[2,0]))/((m[1]**2-m[0]**2)*\
                                (m[2]**2-m[1]**2)*(m[2]**2-m[0]**2)*np.sin(2*Theta_12)*\
                                np.sin(2*Theta_23)*np.sin(2*Theta_13)*np.cos(Theta_13))
            if -1.0 <= alpha <= 1.0:
                Delta_CP = np.arcsin(alpha)
            else:
                Delta_CP = 50
                print('exception: cannot calculate DeltaCP')
        else: 
            Delta_CP = 50
            print('exception: cannot calculate DeltaCP')
        
        #mass differences
        Del_m21Sqr = (m[1]**2-m[0]**2)*10**(5)*10**(18)
        Del_m31Sqr = np.abs((m[2]**2-m[0]**2))*10**(3)*10**(18)
            
            
        Theta_12 = np.degrees(Theta_12)
        Theta_23 = np.degrees(Theta_23)
        Theta_13 = np.degrees(Theta_13)
        

        effMaj = np.abs(U[0,0]**2*m[0]+U[0,1]**2*m[1]+U[0,2]**2*m[2])
        print('')
        print('The light neutrinos feature...')
        print('Del_m21Sqr [10^-5 eV^2]:', Del_m21Sqr)
        print('Del_m31Sqr [10^-3 eV^2]:', Del_m31Sqr)
        print('Theta_12 [deg]         :', Theta_12)
        print('Theta_23 [deg]         :', Theta_23)
        print('Theta_13 [deg]         :', Theta_13)
        print('Delta_CP [rad]         :', Delta_CP)
        print('m_tot [eV]             :', np.sum(m[:])*10**9) 
        print('')
        #obtain the mixing matrix Wrot
        W, hold = Wrot(M_nu, M_D, M_R, U, V)
        print('masses of N_i:', mH[:])
        return W[:,:], M_nu, M_R, mH[0], mH[1], mH[2]

def Wrot(M_nu, M_D, M_R, U, V):
     # we are free too choose the phase appropriately such that masses are real
    Mdiag_nu = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    Mdiag_nu =  np.transpose(np.conjugate(U)) @ M_nu @np.conjugate(U)
    Mnu_pha = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    Unew = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    
    for i in range(3):
        Mnu_pha[i,i] = np.exp(complex(0,np.angle(Mdiag_nu[i,i])/2))
        
    Unew = U@Mnu_pha
    
    Mdiag_R = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    Mdiag_R =  np.transpose(np.conjugate(V)) @ M_R @np.conjugate(V)
    MR_pha = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    Vnew = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    
    for i in range(3):
        MR_pha[i,i] = np.exp(complex(0,np.angle(Mdiag_R[i,i])/2))
        
    Vnew = V@MR_pha

    Rstar = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    R = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    Rdag = np.complex128([[0,0,0],[0,0,0],[0,0,0]])

    Rstar = M_D @ np.linalg.inv(M_R)
    R = np.conjugate(Rstar)
    Rdag = np.transpose(Rstar)
    RT = np.transpose(R)
    
    unity = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    unity[0,0] =1.
    unity[1,1] =1.
    unity[2,2] =1.

    U2_ll = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    U2_lr = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    U2_rl = np.complex128([[0,0,0],[0,0,0],[0,0,0]])
    U2_rr = np.complex128([[0,0,0],[0,0,0],[0,0,0]])

    U2_ll = (unity-1/2*R@Rdag)@np.conjugate(Unew)
    U2_lr = R@np.conjugate(Vnew)
    U2_rl = -Rdag@np.conjugate(Unew)

    U2_rr = (unity-1/2*Rdag@R)@np.conjugate(Vnew)



    W_r = np.complex128([[U2_ll[0,0],U2_ll[0,1],U2_ll[0,2],U2_lr[0,0],U2_lr[0,1],U2_lr[0,2]],\
                                [U2_ll[1,0],U2_ll[1,1],U2_ll[1,2],U2_lr[1,0],U2_lr[1,1],U2_lr[1,2]],\
                                [U2_ll[2,0],U2_ll[2,1],U2_ll[2,2],U2_lr[2,0],U2_lr[2,1],U2_lr[2,2]],\
                                [U2_rl[0,0],U2_rl[0,1],U2_rl[0,2],U2_rr[0,0],U2_rr[0,1],U2_rr[0,2]],\
                                [U2_rl[1,0],U2_rl[1,1],U2_rl[1,2],U2_rr[1,0],U2_rr[1,1],U2_rr[1,2]],\
                                [U2_rl[2,0],U2_rl[2,1],U2_rl[2,2],U2_rr[2,0],U2_rr[2,1],U2_rr[2,2]]])
    W_rot = W_r[:,:]

    return W_rot[:,:], RT
txtBasic = "MZp = Parameter(name = 'MZp',\n \
                nature = 'external',\n \
                type = 'real',\n \
                value = {0:.10e},\n \
                texname = '\\text{{MZp}}',\n \
                lhablock = 'MASS',\n \
                lhacode = [ 9900032 ])\n\
MnH1 = Parameter(name = 'MnH1',\n \
                 nature = 'external',\n \
                 type = 'real',\n \
                 value = {1:.10e},\n \
                 texname = '\\text{{MnH1}}',\n \
                 lhablock = 'MASS',\n \
                 lhacode = [ 9910012 ])\n\
MnH2 = Parameter(name = 'MnH2',\n \
                 nature = 'external',\n \
                 type = 'real',\n \
                 value = {2:.10e},\n\
                 texname = '\\text{{MnH2}}',\n \
                 lhablock = 'MASS',\n \
                 lhacode = [ 9910014 ])\n\
MnH3 = Parameter(name = 'MnH3',\n \
                 nature = 'external',\n \
                 type = 'real',\n \
                 value = {3:.10e},\n \
                 texname = '\\text{{MnH3}}',\n \
                 lhablock = 'MASS',\n \
                 lhacode = [ 9910016 ])\n\
g1p = Parameter(name = 'g1p',\n \
                nature = 'external',\n \
                type = 'real',\n \
                value = {4:.10e},\n \
                texname = 'g_p',\n \
                lhablock = 'LmuLtauINPUTS',\n \
                lhacode = [ 1 ])\n\
MH2 = Parameter(name = 'MH2',\n \
                nature = 'external',\n \
                type = 'real',\n \
                value = {5:.10e},\n \
                texname = '\\text{{MH2}}',\n \
                lhablock = 'MASS',\n \
                lhacode = [ 9900026 ])\n\
Sa = Parameter(name = 'Sa',\n \
               nature = 'external',\n \
               type = 'real',\n \
               value = {6:.10e},\n \
               texname = '\\text{{Sa}}',\n \
               lhablock = 'LmuLtauINPUTS',\n \
               lhacode = [ 3 ])\n"

txtParams = "Mee = Parameter(name = \'Mee\',\n \
                nature = \'external\',\n \
                type = \'real\',\n \
                value = {0:.10e},\n \
                texname = \'\\text{{Mee}}\',\n \
                lhablock = \'LmuLtauINPUTS\',\n \
                lhacode = [ 4 ])\n\
Vemu = Parameter(name = \'Vemu\',\n \
                 nature = \'external\',\n \
                 type = \'real\',\n \
                 value = {1:.10e},\n \
                 texname = \'\\text{{Vemu}}\',\n \
                 lhablock = \'LmuLtauINPUTS\',\n \
                 lhacode = [ 5 ])\n\
Vetau = Parameter(name = \'Vetau\',\n \
                  nature = \'external\',\n \
                  type = \'real\',\n \
                  value = {2:.10e},\n \
                  texname = \'\\text{{Vetau}}\',\n \
                  lhablock = \'LmuLtauINPUTS\',\n \
                  lhacode = [ 6 ])\n\
Mmutau = Parameter(name = \'Mmutau\',\n \
                   nature = \'external\',\n \
                   type = \'real\',\n \
                   value = {3:.10e},\n \
                   texname = \'\\text{{Mmutau}}\',\n \
                   lhablock = \'LmuLtauINPUTS\',\n \
                   lhacode = [ 7 ])\n\
Ximt = Parameter(name = \'Ximt\',\n \
                 nature = \'external\',\n \
                 type = \'real\',\n \
                 value = {4:.10e},\n \
                 texname = \'\\text{{Ximt}}\',\n \
                 lhablock = \'LmuLtauINPUTS\',\n \
                 lhacode = [ 8 ])\n\
fe = Parameter(name = \'fe\',\n \
               nature = \'external\',\n \
               type = \'real\',\n \
               value = {5:.10e},\n \
               texname = \'\\text{{fe}}\',\n \
               lhablock = \'LmuLtauINPUTS\',\n \
               lhacode = [ 9 ])\n\
fmu = Parameter(name = \'fmu\',\n \
                nature = \'external\',\n \
                type = \'real\',\n \
                value = {6:.10e},\n \
                texname = \'\\text{{fmu}}\',\n \
                lhablock = \'LmuLtauINPUTS\',\n \
                lhacode = [ 10 ])\n\
ftau = Parameter(name = \'ftau\',\n \
                 nature = \'external\',\n \
                 type = \'real\',\n \
                 value = {7:.10e},\n \
                 texname = \'\\text{{ftau}}\',\n \
                 lhablock = \'LmuLtauINPUTS\',\n \
                 lhacode = [ 11 ])\n"

txtW = "WRROT{0}{1} = Parameter(name = \'WRROT{0}{1}\',\n \
                    nature = \'external\',\n \
                    type = \'real\',\n \
                    value = {2:.20e},\n \
                    texname = \'\\text{{IWRROT}}\',\n \
                    lhablock = \'WRROT\',\n \
                    lhacode = [ {3} ])\n"

txtIW = "IWRROT{0}{1} = Parameter(name = \'IWRROT{0}{1}\',\n \
                    nature = \'external\',\n \
                    type = \'real\',\n \
                    value = {2:.20e},\n \
                        texname = \'\\text{{IWRROT}}\',\n \
                    lhablock = \'IWRROT\',\n \
                    lhacode = [ {3} ])\n"



#writes input for the parameters.py file of the UFO.
#output is stored in parametersPy.txt
def writePyParam(M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau):
    print('Calculate mixing matrix...')
    W, M_nu, M_R, MN1, MN2, MN3 = WCalc(M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau)
    
    f = open(r"paramatersPy.txt", 'a')
    f.close()
    f = open(r"paramatersPy.txt", 'w')
    f.write(txtBasic.format(MZp, MN1, MN2, MN3, gmutau, MH2, Sa))
    f.write(txtParams.format(M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau))
    for i in range(6):
        for j in range(6):
            f.write(txtW.format(i+1,j+1,np.real(W[i,j]),6*(i)+j+1))
    for i in range(6):
        for j in range(6):
            f.write(txtIW.format(i+1,j+1,np.imag(W[i,j]),6*(i)+j+1))
    f.close()
    print('Output is stored in parametersPy.txt')
    

writePyParam(M_ee, V_emu, V_etau, M_mutau, Xi, f_e, f_mu, f_tau)
