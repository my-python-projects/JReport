// Funções de validação simples

export function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
  
export function validatePassword(password) {
    const re = /^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9]).{6,}$/;
    return re.test(String(password));
}
  