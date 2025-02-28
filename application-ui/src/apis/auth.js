import axios from '@/utils/request.js'

export function login_by_basic_auth(data) {
    return axios(
        {
            method: 'post',
            url: '/auth/login',
            headers: {'Content-Type': 'application/json'},
            rejectUnauthorized: false,
            data
        }
    )
}


export function change_password(data) {
    return axios(
        {
            method: 'post',
            url: 'auth/change_password',
            headers: {'Content-Type': 'application/json'},
            rejectUnauthorized: false,
            data
        }
    )
}
