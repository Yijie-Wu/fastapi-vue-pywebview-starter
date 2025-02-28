import axios from '@/utils/request.js'

export function get_years() {
    return axios(
        {
            method: 'get',
            url: `/year/all`,
        }
    )
}

export function add_year(data) {
    return axios(
        {
            method: 'post',
            url: '/year/create',
            data
        }
    )
}

export function update_year(id, data) {
    return axios(
        {
            method: 'patch',
            url: `/year/update/${id}`,
            data
        }
    )
}


export function update_year_photo(id, data) {
    return axios(
        {
            method: 'patch',
            url: `/year/update/photo/${id}`,
            data
        }
    )
}

export function delete_year(id) {
    return axios(
        {
            method: 'delete',
            url: '/year/delete/' + id
        }
    )
}


export function delete_year_photo(id) {
    return axios(
        {
            method: 'delete',
            url: '/year/delete/photo/' + id
        }
    )
}
