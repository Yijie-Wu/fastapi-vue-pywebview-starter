import axios from '@/utils/request.js'


export function get_admin_message() {
    return axios(
        {
            method: 'get',
            url: '/message/admin',
        }
    )
}

export function get_years_photos_message() {
    return axios(
        {
            method: 'get',
            url: '/message/years-photos',
        }
    )
}

export function get_year_photos_message(id) {
    return axios(
        {
            method: 'get',
            url: '/message/year_photos/' + id,
        }
    )
}

export function search_photos(q) {
    return axios(
        {
            method: 'get',
            url: '/message/photos/search?q=' + q,
        }
    )
}
