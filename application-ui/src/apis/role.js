import axios from '../utils/request.js';


export function get_roles() {
    return axios(
        {
            method: 'get',
            url: '/role/all',
        }
    )
}
