import axios from '@/utils/request.js'


export function get_carousels() {
    return axios(
        {
            method: 'get',
            url: `/carousels/all`,
        }
    )
}

export function get_show_carousels() {
    return axios(
        {
            method: 'get',
            url: '/carousels/all/show',
        }
    )
}

export function add_carousels(data) {
    return axios(
        {
            method: 'post',
            url: '/carousels/create',
            data
        }
    )
}

export function update_carousels(id, data) {
    return axios(
        {
            method: 'patch',
            url: `/carousels/update/${id}`,
            data
        }
    )
}

export function delete_carousels(id) {
    return axios(
        {
            method: 'delete',
            url: '/carousels/delete/' + id
        }
    )
}
