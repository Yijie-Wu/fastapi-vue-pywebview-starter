import {ElMessage, ElNotification} from 'element-plus'

export function showMessage(type, message, duration = 3000) {
    ElMessage({
        type: type,
        message: message,
        duration: duration,
    })
}


export function showNotification(title, message, type, duration, position) {
    ElNotification({
        title: title,
        message: message,
        type: type,
        duration: duration,
        position: position,
    })
}
