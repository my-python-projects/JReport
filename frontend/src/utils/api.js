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
