import axios from '@/utils/request.js'

export function get_settings() {
    return axios(
        {
            method: 'get',
            url: 'codex/settings/all',
        }
    )
}

export function get_setting_by_id(id) {
    return axios(
        {
            method: 'get',
            url: 'codex/settings/setting/id/' + id,
        }
    )
}

export function get_setting_by_name(name) {
    return axios(
        {
            method: 'get',
            url: 'codex/settings/setting/name/' + name,
        }
    )
}

export function add_settings(data) {
    return axios(
        {
            method: 'post',
            url: 'codex/settings/add/setting',
            headers: {'Content-Type': 'application/json'},
            data
        }
    )
}

export function update_settings(id, data) {
    return axios(
        {
            method: 'patch',
            url: 'codex/settings/update/setting/' + id,
            headers: {'Content-Type': 'application/json'},
            data
        }
    )
}

export function delete_settings(id) {
    return axios(
        {
            method: 'delete',
            url: 'codex/settings/delete/setting/' + id,
        }
    )
}

