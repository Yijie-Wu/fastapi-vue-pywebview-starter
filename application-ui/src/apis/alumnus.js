import axios from '@/utils/request.js'


export function get_alumnus(skip, limit) {
    return axios(
        {
            method: 'get',
            url: `/alumnus/all?skip=${skip}&limit=${limit}`,
        }
    )
}

export function get_show_alumnus() {
    return axios(
        {
            method: 'get',
            url: '/alumnus/all/show',
        }
    )
}

export function add_alumnus(data) {
    return axios(
        {
            method: 'post',
            url: '/alumnus/create',
            data
        }
    )
}

export function update_alumnus(id, data) {
    return axios(
        {
            method: 'patch',
            url: `/alumnus/update/${id}`,
            data
        }
    )
}

export function delete_alumnus(id) {
    return axios(
        {
            method: 'delete',
            url: '/alumnus/delete/' + id
        }
    )
}

export function search_alumnus(data) {
    return axios(
        {
            method: 'post',
            url: '/search/alumnus/all',
            data
        }
    )
}

export function search_alumnus_history() {
    return axios(
        {
            method: 'get',
            url: '/search/alumnus/history'
        }
    )
}

export function clear_alumnus() {
    return axios(
        {
            method: 'delete',
            url: '/search/alumnus/clear'
        }
    )
}
