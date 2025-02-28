import axios from '@/utils/request.js'


export function get_userinfo() {
    return axios(
        {
            method: 'get',
            url: '/user/current_user/info',
        }
    )
}

export function get_users() {
    return axios(
        {
            method: 'get',
            url: '/user/all',
        }
    )
}

export function update_profile(data) {
    return axios(
        {
            method: 'post',
            url: '/user/update/profile',
            data
        }
    )
}

export function change_user_password(data) {
    return axios(
        {
            method: 'post',
            url: '/user/change-password',
            data
        }
    )
}

export function change_avatar(data) {
    return axios(
        {
            method: 'post',
            url: '/user/change-avatar',
            data
        }
    )
}

export function add_user(data) {
    return axios(
        {
            method: 'post',
            url: '/user/add',
            data
        }
    )
}

export function update_user(id, data) {
    return axios(
        {
            method: 'patch',
            url: '/user/update/' + id,
            data
        }
    )
}

export function delete_user(id) {
    return axios(
        {
            method: 'delete',
            url: '/user/delete/' + id
        }
    )
}
