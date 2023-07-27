m_hot = 26.6 # g 
Ti_hot = 56.3 # C

m_cold = 28.4 # g
Ti_cold = 26.0 # C

C_h20 = 4.18 # J/gC

Tf_method1 = (m_hot * Ti_hot + m_cold * Ti_cold) / (m_hot + m_cold)
print(Tf_method1)
# print Tf_method1 along with a descriptive message
print("Tf_method1", Tf_method1, "degrees C.")

Tf_method2 = (m_hot*C_h20*Ti_hot + m_cold*C_h20*Ti_cold) / (m_hot*C_h20 + m_cold*C_h20)
# print Tf_method2 along with a descriptive message
print("Tf_method2", Tf_method2, "degrees C.")

measured_final_temp = 40.0 # C

percent_difference = abs((measured_final_temp - Tf_method1) / Tf_method1 * 100)
print("Percent Difference:", percent_difference)


