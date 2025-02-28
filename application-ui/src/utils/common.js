let api_server = 'http://127.0.0.1:8000'

export function calcAvatar(avatar = 'default-avatar.png') {
    return `${api_server}/user/avatar/${avatar}`
}

export function calcAvatarByID(id) {
    return 'http://127.0.0.1:8000/user/avatar/id/' + id
}

export function calcFile(image, file_type='file') {
    return `${api_server}/download/${file_type}/${image}`
}

export function JSON_Validate(json) {
    try {
        JSON.parse(json)
        return true
    } catch (e) {
        return false
    }
}
