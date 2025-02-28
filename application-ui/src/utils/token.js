export function setToken(token) {
    return localStorage.setItem('token', token);
}

export function getToken() {
    return localStorage.getItem('token');
}

export function removeToken() {
    return localStorage.removeItem('token');
}

export function isLoginedUser() {
    let token = getToken()
    return token !== null && token !== ''
}
