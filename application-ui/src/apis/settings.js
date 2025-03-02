import axios from '@/utils/request.js'

export function get_setting() {
    return axios(
        {
            method: 'get',
            url: '/config/setting'
        }
    )
}

export function update_setting(data) {
    return axios(
        {
            method: 'put',
            url: '/config/setting',
            data
        }
    )
}



