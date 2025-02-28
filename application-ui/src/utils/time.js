import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime';

dayjs.extend(relativeTime);

export function formatDate(date) {
    return dayjs(date).format('YYYY-MM-DD HH:mm:ss')
}

export function formatDateFromNow(date) {
    return dayjs(date).fromNow();
}

