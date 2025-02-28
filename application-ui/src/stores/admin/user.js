import {defineStore} from "pinia";

export const useAllUsersStore = defineStore('allUsersStore', {
    state() {
        return {
            users: [],
        }
    },
    actions: {
        setUsers(data) {
            this.users = data;
        },
        addUser(data) {
            this.users.push(data);
        },
        removeUser(id) {
            this.users = this.users.filter(user => user.id !== id);
        },
        updateUser(data) {
            this.users = this.users.map(user => {
                if (user.id === data.id) {
                    return data;
                }
                return user;
            });
        }
    }
})
