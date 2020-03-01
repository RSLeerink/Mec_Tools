




#Chapter_9_Local_buckling_of_stiffeners_girders_brackets


#Checks
#9.1.1
#Welded_section = 

#7.2 


#(7.1) - Equvilant axial force
A_s = 200*50
s = 100
t = 5
E = 210000 #Mpa
l = 100 #See fig 7-1
L_G = 200#m
Sigma_x_Sd = 100 #Input
tau_Sd = 25 #Design shear stres


#Factors
gamma_M = 1.0

#(7.7)
if l >= s:
    k_l = 5.34 + 4*(s/l)**2
elif l < s:
    5.34 * (s/l)**2 + 4

#(7.6)
tau_crl = k_l * 0.904*E*(t/s)**2

#(7.5)
if l <= L_G :
    k_g = 5.34 + 4*(l/L_G)**2
elif l > L_G:
    k_g = 5.34 * (l/L_G)**2 + 4

#(7.4)
tau_erg = k_g * 0.904 * E * (t/l)**2

if tau_Sd < tau_crl/gamma_M:
    tau_tf = tau_Sd - tau_erg
else:
    tau_tf = 0

N_Sd = Sigma_x_Sd * (A_s + s*t) + tau_tf * s * t

print(tau_erg)