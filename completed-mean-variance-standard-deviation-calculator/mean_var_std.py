import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError ("List must contain nine numbers.")

  mat3x3 = np.array(list).reshape((3,3))
  
  m_axis1 = np.mean(mat3x3, axis=0).tolist()
  m_axis2 = np.mean(mat3x3, axis=1).tolist()
  m_flat = np.mean(mat3x3)
  
  v_ax1 = np.var(mat3x3, axis=0).tolist()
  v_ax2 = np.var(mat3x3, axis=1).tolist()
  v_flat = np.var(mat3x3)

  sd_ax1 = np.std(mat3x3, axis=0).tolist()
  sd_ax2 = np.std(mat3x3, axis=1).tolist()
  sd_flat = np.std(mat3x3)

  mx_ax1 = np.max(mat3x3, axis=0).tolist()
  mx_ax2 = np.max(mat3x3, axis=1).tolist()
  mx_flat = np.max(mat3x3)

  mn_ax1 = np.min(mat3x3, axis=0).tolist()
  mn_ax2 = np.min(mat3x3, axis=1).tolist()
  mn_flat = np.min(mat3x3)

  sm_ax1 = np.sum(mat3x3, axis=0).tolist()
  sm_ax2 = np.sum(mat3x3, axis=1).tolist()
  sm_flat = np.sum(mat3x3)
  
  calculations = {
    'mean': [m_axis1, m_axis2, m_flat],
    'variance': [v_ax1, v_ax2, v_flat],
    'standard deviation': [sd_ax1, sd_ax2, sd_flat],
    'max': [mx_ax1, mx_ax2, mx_flat],
    'min': [mn_ax1, mn_ax2, mn_flat],
    'sum': [sm_ax1, sm_ax2, sm_flat]
  }

  return calculations