import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export async function registerUser(userData) {
  try {
    const response = await axios.post(`${API_URL}/register`, userData);
    return response.data;
  } catch (error) {
    console.error("Error registering user:", error);
    throw error;
  }
}

export async function loginUser(userData) {
  try {
    const response = await axios.post(`${API_URL}/login`, userData);
    return response.data;
  } catch (error) {
    console.error("Error logging in user:", error);
    throw error;
  }
}

export async function submitReport(reportData) {
  try {
    const response = await axios.post(`${API_URL}/report`, reportData);
    return response.data;
  } catch (error) {
    console.error('Error submitting report:', error);
    throw error;
  }
}

export const verify2fa = async (verificationData) => {
  try {
    const response = await axios.post(`${API_URL}/verify-2fa`, verificationData);
    return response.data;
  } catch (error) {
    console.error('Error verifying 2FA:', error);
    throw error;
  }
};

export const check2FA = async (data) => {
  try {
    const response = await axios.post(`${API_URL}/check-2fa`, data);
    return response.data;
  } catch (error) {
    console.error('Error checking 2FA:', error);
    throw error;
  }
};
